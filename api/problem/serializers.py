from .models import BigSubject, SmallSubject, Region, Problem, TestSet, RealRegion
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


# 소주제
class ProblemSmallSubjectSerializer(serializers.ModelSerializer):
    color = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = SmallSubject
        fields = ['id', 'title', 'color']

    def get_color(self, obj):
        return obj.color


# 문제 리스트, 문제 디테일까지.
class ProblemListSerializer(serializers.ModelSerializer):
    is_scrapped = serializers.SerializerMethodField(read_only=True)
    type = serializers.CharField(read_only=True, source='get_type_display')
    region = serializers.SerializerMethodField(read_only=True)
    big_subject = serializers.StringRelatedField(many=False, read_only=True)
    size = serializers.SerializerMethodField(read_only=True)
    presentation_image = serializers.SerializerMethodField(read_only=True)
    small_subjects = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Problem
        fields = ['id', 'title', 'number', 'type', 'region', 'big_subject', 'small_subjects',
                  'presentation', 'question', 'answer', 'is_scrapped', 'presentation_image', 'size']

    def get_small_subjects(self, obj):
        temp_data = list(ProblemSmallSubjectSerializer(obj.small_subject, many=True).data)

        # 문제 유형
        if obj.problem_type == 'P':
            temp_data.append({'id': 1, 'title': '연습문제', 'color': '65b1e5'})
        else:
            temp_data.append({'id': 2, 'title': '실전문제', 'color': '65b1e5'})

        # 문제 유형
        if obj.type == 'A':
            temp_data.append({'id': 3, 'title': '구상형', 'color': '65b1e5'})
        elif obj.type == 'B':
            temp_data.append({'id': 4, 'title': '즉답형', 'color': '65b1e5'})
        elif obj.type == 'C':
            temp_data.append({'id': 5, 'title': '추가질문', 'color': '65b1e5'})

        # 지역 기반
        if obj.region.title == '서울':
            temp_data.append({'id': 6, 'title': '서울', 'color': '65b1e5'})
        elif obj.region.title == '경기':
            temp_data.append({'id': 7, 'title': '경기', 'color': '65b1e5'})
        elif obj.region.title == '세종':
            temp_data.append({'id': 8, 'title': '세종', 'color': '65b1e5'})
        elif obj.region.title == '평가원':
            temp_data.append({'id': 9, 'title': '평가원', 'color': '65b1e5'})
        else:
            temp_data.append({'id': 9, 'title': '공통', 'color': '65b1e5'})

        return temp_data

    def get_is_scrapped(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return user in obj.scrapped_users.all()
        else:
            return False

    def get_region(self, obj):
        return obj.region.title

    def get_size(self, obj):
        try:
            width, height = obj.width, obj.height
            return {'width': width, 'height': height}
        except:
            return {'width': None, 'height': None}

    def get_presentation_image(self, obj):
        if obj.image_url is None:
            if obj.presentation_image:
                return obj.presentation_image.url
            return None
        return obj.image_url


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


# 실전 모의고사 설명
class TestSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestSet
        fields = ['id', 'description', 'time_description']
