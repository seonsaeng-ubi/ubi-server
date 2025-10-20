from .models import StudyRoom, Region, Problem
from django.db.models import Q, Value
from django.conf import settings
import random
import secrets


def generate_unique_room_no():
    while True:
        number = str(random.randint(10000, 99999))  # 5자리 숫자
        if not StudyRoom.objects.filter(room_no=number).exists():
            return number


def build_deep_link(token: str) -> str:
    return f'https://woobi.co.uk/s/study/room/{token}'


def get_random_practice_problems(region_id: int, problem_type: str):
    regions = Region.objects.all()
    pyeonggawon = regions.get(title='평가원')
    gongtong = regions.get(title='공통')
    region = regions.get(id=region_id)

    # 평가원일 경우
    if region.id == pyeonggawon.id:
        problems = Problem.objects.filter(
            Q(region=region) & Q(type=problem_type) & Q(problem_type='P')
        )
    # 그 외의 경우
    else:
        problems = Problem.objects.filter(
            (Q(region=region) | Q(region=gongtong)) & Q(type=problem_type) & Q(problem_type='P')
        )
    return problems.order_by('?')[:3]


def get_mockup_problems(region_id: int):
    # 지역 필터링
    regions = Region.objects.all()
    seoul = regions.get(title='서울')
    gyeonggi = regions.get(title='경기')
    # sejong = regions.get(title='세종')
    pyeonggawon = regions.get(title='평가원')
    gongtong = regions.get(title='공통')
    region = regions.get(id=region_id)

    # 공통이거나 특정 지역일 경우 우선 필터링
    if region.id == pyeonggawon.id:
        problems = Problem.objects.filter(region=region)
    else:
        problems = Problem.objects.filter(Q(region=region) | Q(region=gongtong))
    # 서울일 경우
    if region.id == seoul.id:
        # 구상형 3문제, 즉답형 3, 추가 질문 2
        conception = problems.filter(type='A').order_by('?')[:2]
        immediate = problems.filter(type='B').order_by('?')[:3]
        # additional = problems.filter(type='C').order_by('?')[:2]

        type_a = conception.annotate(custom_order=Value(1))
        type_b = immediate.annotate(custom_order=Value(2))
        # type_c = additional.annotate(custom_order=Value(3))
        result = type_a.union(type_b).order_by('custom_order')
        # result = temp_result.union(type_c).order_by('custom_order')

        return result
    # 경기일 경우
    elif region.id == gyeonggi.id:
        # 구상형 3문제, 즉답형 2
        conception = problems.filter(type='A').order_by('?')[:3]
        immediate = problems.filter(type='B').order_by('?')[:2]

        type_a = conception.annotate(custom_order=Value(1))
        type_b = immediate.annotate(custom_order=Value(2))
        result = type_a.union(type_b).order_by('custom_order')

        return result
    # 평가원일 경우
    else:
        # 구상형 3문제, 즉답형 1
        conception = problems.filter(type='A').order_by('?')[:3]
        immediate = problems.filter(type='B').order_by('?')[:1]

        type_a = conception.annotate(custom_order=Value(1))
        type_b = immediate.annotate(custom_order=Value(2))
        result = type_a.union(type_b).order_by('custom_order')

        return result
