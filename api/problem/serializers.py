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
    type = serializers.CharField(read_only=True, source='get_type_display')
    region = serializers.SerializerMethodField(read_only=True)
    big_subject = serializers.StringRelatedField(many=False, read_only=True)
    small_subject = serializers.StringRelatedField(many=True, read_only=True)

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

    def get_region(self, obj):
        return obj.region.title


# 실전 문제 세트
class RealProblemSetSerializer(serializers.ModelSerializer):
    class SmallProblemSerializer(serializers.ModelSerializer):
        class Meta:
            model = Problem
            fields = ['id', 'title']

    problems = SmallProblemSerializer(many=True, read_only=True, source='problem_problem_set')

    class Meta:
        model = ProblemSet
        fields = ['id', 'title', 'description', 'problems']


# 문제 스크랩 / 해제
class ProblemUpdateSerializer(serializers.ModelSerializer):
    is_scrapped = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Problem
        fields = ['id', 'is_scrapped']

    def get_is_scrapped(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return user in obj.scrapped_users.all()
        else:
            return False

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if not user.is_authenticated:
            return ValidationError({'error_msg': '스크랩을 하려면 로그인 해야 합니다.'})
        if user in instance.like_users.all():
            instance.scrapped_users.remove(user)
        else:
            instance.scrapped_users.add(user)
        return instance
