import datetime
import random
import hashlib
from django.db import transaction
from django.utils import timezone
from rest_framework import serializers
from api.logger.models import EmailLog
from api.user.validators import validate_password
from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.exceptions import ValidationError as DjangoValidationError
from api.user.models import User, EmailVerifier, SocialKindChoices, Profile


class UserSocialLoginSerializer(serializers.Serializer):
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    code = serializers.CharField(write_only=True)
    email = serializers.CharField(write_only=True)
    nickname = serializers.CharField(write_only=True)
    phone = serializers.CharField(write_only=True, allow_null=True, allow_blank=True)
    firebase_token = serializers.CharField(write_only=True)
    social_type = serializers.CharField(write_only=True)

    def validate(self, attrs):
        code = attrs['code']
        email = attrs['email']
        nickname = attrs['nickname']
        phone = attrs['phone']
        social_type = attrs['social_type']
        firebase_token = attrs['firebase_token']

        if social_type not in SocialKindChoices:
            raise ValidationError({'kind': '지원하지 않는 소셜 타입입니다.'})

        return attrs

    @transaction.atomic
    def create(self, validated_data):
        code = validated_data['code']
        email = validated_data['email']
        nickname = validated_data['nickname']
        phone = validated_data['phone']
        social_type = validated_data['social_type']
        firebase_token = validated_data['firebase_token']
        user, created = User.objects.get_or_create(email=email, defaults={'password': make_password(None)})

        if created:
            user_profile = Profile.objects.create(user=user, nickname=nickname, kind=social_type, code=code, phone=phone, firebase_token=firebase_token)
            user_profile.save()
        else:
            user_profile = Profile.objects.get(user=user)
            user_profile.firebase_token = firebase_token
            user_profile.save()

        refresh = RefreshToken.for_user(user)

        return {
            'access': refresh.access_token,
            'refresh': refresh,
        }


class UserRegisterSerializer(serializers.Serializer):
    email = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    def validate(self, attrs):
        email = attrs.get('email')

        if 'email' in User.REGISTER_FIELDS:
            if User.objects.filter(email=email).exists():
                raise ValidationError({'email': ['이미 가입된 이메일입니다.']})
        return attrs

    @transaction.atomic
    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']
        user, created = User.objects.get_or_create(email=email, defaults={'password': make_password(password)})

        if created:
            user_profile = Profile.objects.create(user=user, nickname='')
            user_profile.save()

        refresh = RefreshToken.for_user(user)

        return {
            'access': refresh.access_token,
            'refresh': refresh,
        }


class ProfileSerializer(serializers.ModelSerializer):
    marketing_agreed_at = serializers.CharField(read_only=True)

    class Meta:
        model = Profile
        fields = ['nickname', 'firebase_token', 'terms_agreed', 'marketing_agreed', 'marketing_agreed_at']

    def validate(self, attrs):
        terms_agreed = attrs.get('terms_agreed')
        if bool(terms_agreed) is False:
            raise ValidationError({'error': ['약관 동의가 필요합니다.']})
        return attrs

    def update(self, instance, validated_data):
        instance.nickname = validated_data.get('nickname', instance.nickname)
        instance.terms_agreed = validated_data.get('terms_agreed', instance.terms_agreed)
        instance.firebase_token = validated_data.get('firebase_token', instance.firebase_token)
        if instance.marketing_agreed != bool(validated_data.get('marketing_agreed', instance.marketing_agreed)):
            instance.marketing_agreed_at = datetime.datetime.now()
        instance.marketing_agreed = bool(validated_data.get('marketing_agreed', instance.marketing_agreed))
        instance.save()
        return instance


class UserDetailUpdateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    password = serializers.CharField(write_only=True, allow_blank=True)
    password_confirm = serializers.CharField(write_only=True, allow_blank=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'password', 'password_confirm']

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.get('password_confirm')

        errors = {}

        # 이메일 검증
        if self.instance.is_social:
            attrs['email'] = self.instance.email

        # 비밀번호 검증
        if password or password_confirm:
            if password != password_confirm:
                errors['password'] = ['비밀번호가 일치하지 않습니다.']
                errors['password_confirm'] = ['비밀번호가 일치하지 않습니다.']
            else:
                try:
                    validate_password(password)
                except DjangoValidationError as error:
                    errors['password'] = list(error)
                    errors['password_confirm'] = list(error)
            attrs['password'] = make_password(password)
        else:
            attrs['password'] = self.instance.password

        if errors:
            raise ValidationError(errors)

        return attrs

    @transaction.atomic
    def update(self, instance, validated_data):
        instance.__dict__.update(validated_data)
        instance.save()
        return instance


class EmailVerifierCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailVerifier
        fields = ['email']

    def validate(self, attrs):
        email = attrs['email']

        if User.objects.filter(email=email).exists():
            raise ValidationError({'email': ['이미 존재하는 이메일입니다.']})

        code = ''.join([str(random.randint(0, 9)) for i in range(6)])
        created = timezone.now()
        hash_string = str(email) + code + str(created.timestamp())
        token = hashlib.sha1(hash_string.encode('utf-8')).hexdigest()

        attrs.update({
            'code': code,
            'token': token,
            'created': created,
        })

        try:
            self.send_code(attrs)
        except Exception:
            raise ValidationError('인증번호 전송 실패')

        return attrs

    def send_code(self, attrs):
        body = f'선생우비 회원가입 인증번호: [{attrs["code"]}]'
        EmailLog.objects.create(to=attrs['email'], body=body)


class EmailVerifierConfirmSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    code = serializers.CharField(write_only=True)
    email_token = serializers.CharField(read_only=True, source='token')

    class Meta:
        model = EmailVerifier
        fields = ['email', 'code', 'email_token']

    def validate(self, attrs):
        email = attrs['email']
        code = attrs['code']
        try:
            email_verifier = self.Meta.model.objects.get(email=email, code=code)
        except self.Meta.model.DoesNotExist:
            raise ValidationError({'code': ['인증번호가 일치하지 않습니다.']})

        attrs.update({'token': email_verifier.token})
        return attrs

    def create(self, validated_data):
        return validated_data
