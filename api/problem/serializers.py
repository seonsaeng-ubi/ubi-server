from .models import BigSubject, SmallSubject, Region, ProblemSet, Problem
from rest_framework.exceptions import ValidationError
from rest_framework import serializers
import random


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


# 문제 리스트, 문제 디테일까지.
class ProblemListSerializer(serializers.ModelSerializer):
    is_scrapped = serializers.SerializerMethodField(read_only=True)
    type = serializers.CharField(read_only=True, source='get_type_display')
    region = serializers.SerializerMethodField(read_only=True)
    big_subject = serializers.StringRelatedField(many=False, read_only=True)

    class ProblemSmallSubjectSerializer(serializers.ModelSerializer):
        color = serializers.SerializerMethodField(read_only=True)

        class Meta:
            model = SmallSubject
            fields = ['id', 'title', 'color']

        def get_color(self, obj):
            chars = '0123456789ABCDEF'
            return '0xff' + ''.join(random.sample(chars, 6))

    small_subjects = ProblemSmallSubjectSerializer(many=True, read_only=True, source='small_subject')

    class Meta:
        model = Problem
        fields = ['id', 'title', 'number', 'type', 'region', 'big_subject',
                  'small_subjects', 'presentation', 'question', 'answer', 'is_scrapped']

    def get_is_scrapped(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return user in obj.scrapped_users.all()
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

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        problem_model = instance.problem_problem_set
        representation['conception'] = problem_model.filter(type='A').count()
        representation['immediate'] = problem_model.filter(type='B').count()
        representation['additional'] = problem_model.filter(type='C').count()
        return representation


# 문제 스크랩 / 해제
class ProblemUpdateSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
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
        if user in instance.scrapped_users.all():
            instance.scrapped_users.remove(user)
        else:
            instance.scrapped_users.add(user)
        return instance
