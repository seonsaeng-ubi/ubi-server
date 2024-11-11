from .models import BigSubject, SmallSubject, Region, Problem, TestSet, Color
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
    number = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Problem
        fields = ['id', 'title', 'number', 'type', 'region', 'big_subject', 'small_subjects',
                  'presentation', 'question', 'answer', 'is_scrapped', 'presentation_image', 'size']

    def get_number(self, obj):
        return str(obj.number)

    def get_small_subjects(self, obj):
        temp_data = list(ProblemSmallSubjectSerializer(obj.small_subject, many=True).data)
        colors = Color.objects.all()
        color1, color2, color3 = '', '', ''

        # 문제 유형
        if obj.problem_type == 'P':
            color1 = colors.get(title='연습문제')
        else:
            color1 = colors.get(title='기출문제')
        temp_data.append({'id': color1.id, 'title': color1.title, 'color': color1.color})

        # 문제 유형
        if obj.type == 'A':
            color2 = colors.get(title='구상형')
        elif obj.type == 'B':
            color2 = colors.get(title='즉답형')
        elif obj.type == 'C':
            color2 = colors.get(title='추가질문')
        temp_data.append({'id': color2.id, 'title': color2.title, 'color': color2.color})

        # 지역 기반
        if obj.region.title == '서울':
            color3 = colors.get(title='서울')
        elif obj.region.title == '경기':
            color3 = colors.get(title='경기')
        # elif obj.region.title == '세종':
        #     color3 = colors.get(title='세종')
        elif obj.region.title == '평가원':
            color3 = colors.get(title='평가원')
        else:
            color3 = colors.get(title='공통')
        temp_data.append({'id': color3.id, 'title': color3.title, 'color': color3.color})

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
