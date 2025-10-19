from rest_framework.generics import CreateAPIView, DestroyAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from api.user.models import Profile

from api.user.serializers import UserRegisterSerializer, ProfileSerializer, \
    UserSocialLoginSerializer, UserDetailUpdateSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
import logging

logger = logging.getLogger(__name__)


class UserSocialLoginView(CreateAPIView):
    serializer_class = UserSocialLoginSerializer


class UserRegisterView(CreateAPIView):
    serializer_class = UserRegisterSerializer


class ProfileDetailUpdateView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    allowed_methods = ['put', 'get']

    def get_object(self):
        return Profile.objects.get(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        try:
            del_user = self.request.user
            del_user.delete()
            return Response(status=HTTP_200_OK)
        except:
            raise ValidationError({'error_msg': '회원 삭제에 실패했습니다.'})


class UserDeleteAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return Profile.objects.get(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        try:
            del_user = self.request.user
            del_user.delete()
            return Response(status=HTTP_200_OK)
        except:
            raise ValidationError({'error_msg': '회원 삭제에 실패했습니다.'})


class AppleSIWANotificationView(APIView):
    """Sign in with Apple 서버-투-서버 알림 수신 엔드포인트.
    - JSON 본문을 수신하고 200 OK를 즉시 반환합니다.
    - Authorization: Bearer <JWT> 헤더가 있으면 Apple JWKS로 서명 검증을 시도합니다(선택).
    """
    permission_classes = [AllowAny]
    authentication_classes = []  # CSRF 미적용(무인증 수신)

    def post(self, request, *args, **kwargs):
        payload = request.data
        verified = False
        verification_error = None
        claims = None

        auth = request.META.get('HTTP_AUTHORIZATION', '')
        if auth.startswith('Bearer '):
            token = auth.split(' ', 1)[1].strip()
            try:
                import jwt
                import json
                import requests
                # 토큰 헤더에서 kid 추출
                header = jwt.get_unverified_header(token)
                kid = header.get('kid')
                # Apple JWKS 가져오기
                r = requests.get('https://appleid.apple.com/auth/keys', timeout=5)
                r.raise_for_status()
                jwks = r.json().get('keys', [])
                key = next((k for k in jwks if k.get('kid') == kid), None)
                if key:
                    public_key = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(key))
                    # 클레임 검증은 선택(서명만 확인). exp/aud/iss 검증 비활성화
                    claims = jwt.decode(
                        token,
                        public_key,
                        algorithms=['RS256'],
                        options={
                            'verify_signature': True,
                            'verify_exp': False,
                            'verify_aud': False,
                            'verify_iss': False,
                        },
                    )
                    verified = True
                else:
                    verification_error = 'No matching kid in Apple JWKS'
            except Exception as e:
                verification_error = str(e)

        # 기본 로깅(운영 환경에선 구조화 로깅/보관 권장)
        logger.info('SIWA S2S notification received', extra={
            'verified': verified,
            'verification_error': verification_error,
            'claims': claims,
            'payload': payload,
            'user_agent': request.META.get('HTTP_USER_AGENT'),
        })

        # 즉시 200 반환(Apple 재시도 방지)
        return Response({'status': 'ok', 'verified': verified}, status=HTTP_200_OK)


# class UserDetailUpdateView(RetrieveUpdateAPIView):
#     serializer_class = UserDetailUpdateSerializer
#     permission_classes = [IsAuthenticated]
#
#     def get_object(self):
#         return self.request.user
