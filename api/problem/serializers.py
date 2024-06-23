from .models import BigSubject, SmallSubject, Region, ProblemSet, Problem
from rest_framework.exceptions import ValidationError
from rest_framework import serializers


# 대주제
class BigSubjectSerializer(serializers.ModelSerializer):
    class SmallSubjectSerializer(serializers.ModelSerializer):
        class Meta:
            model = SmallSubject
            fields = ['id', 'title']

    small_subject = SmallSubjectSerializer(many=True, read_only=True, source='big_small_subjects')

    class Meta:
        model = BigSubject
        fields = ['id', 'title', 'small_subject']


# 지역 리스트
class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'title']


# 문제 리스트
class ProblemListSerializer(serializers.ModelSerializer):
    is_scrapped = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Problem
        fields = ['id', 'title', 'number', 'type', 'region', 'big_subject',
                  'small_subject', 'presentation', 'question', 'answer', 'is_scrapped']

    def get_is_scrapped(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return user in obj.like_users.all()
        else:
            return False


# 실전 문제 세트
class RealProblemSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemSet
        fields = ['id', 'title', 'description', 'type']


# 문제 스크랩 / 해제
class ProblemUpdateSerializer(serializers.ModelSerializer):
    is_scrapped = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Problem
        fields = ['id', 'is_scrapped']

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if not user.is_authenticated:
            return ValidationError({'error_msg': '스크랩을 하려면 로그인 해야 합니다.'})
        if user in instance.like_users.all():
            instance.scrapped_users.remove(user)
        else:
            instance.scrapped_users.add(user)
        return instance
