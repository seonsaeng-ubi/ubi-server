from rest_framework.generics import CreateAPIView, DestroyAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from api.user.models import Profile

from api.user.serializers import UserRegisterSerializer, ProfileSerializer, \
    UserSocialLoginSerializer, UserDetailUpdateSerializer


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


# class UserDetailUpdateView(RetrieveUpdateAPIView):
#     serializer_class = UserDetailUpdateSerializer
#     permission_classes = [IsAuthenticated]
#
#     def get_object(self):
#         return self.request.user
