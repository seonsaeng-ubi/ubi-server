from .models import StudyRoom, Region, Problem
from django.db.models import Q
import random


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

    def pick_and_order(qs, limit):
        # 무작위 선별 후, 해당 집합을 number 기준으로 재정렬
        picked_ids = list(qs.values_list('id', flat=True).order_by('?')[:limit])
        if not picked_ids:
            return Problem.objects.none()
        return Problem.objects.filter(id__in=picked_ids).order_by('number', 'id')

    # 서울일 경우
    if region.id == seoul.id:
        # 구상형 2, 즉답형 3
        conception = pick_and_order(problems.filter(type='A'), 2)
        immediate = pick_and_order(problems.filter(type='B'), 3)
        # 최종: 구상형 먼저, 즉답형 다음
        return list(conception) + list(immediate)
    # 경기일 경우
    elif region.id == gyeonggi.id:
        # 구상형 3문제, 즉답형 2
        conception = pick_and_order(problems.filter(type='A'), 3)
        immediate = pick_and_order(problems.filter(type='B'), 2)
        return list(conception) + list(immediate)
    # 평가원일 경우
    else:
        # 구상형 3문제, 즉답형 1
        conception = pick_and_order(problems.filter(type='A'), 3)
        immediate = pick_and_order(problems.filter(type='B'), 1)
        return list(conception) + list(immediate)
