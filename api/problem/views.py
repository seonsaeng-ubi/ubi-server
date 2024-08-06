from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView, RetrieveAPIView
from .serializers import BigSubjectSerializer, RegionSerializer, \
    ProblemListSerializer, ProblemUpdateSerializer, TestSetSerializer
from .models import BigSubject, Region, Problem, TestSet, RealRegion
from rest_framework.permissions import IsAuthenticated, AllowAny
from ..utils import StandardResultsSetPagination
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from django.db.models import Q


class SubjectAPIView(ListAPIView):
    serializer_class = BigSubjectSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return BigSubject.objects.all()


class RegionAPIView(ListAPIView):
    serializer_class = RegionSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Region.objects.all()[:4]


# 스크랩 취소 / 하기
class ScrapUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = ProblemUpdateSerializer
    permission_classes = [IsAuthenticated]
    queryset = Problem.objects.all()
    allowed_methods = ['put', 'get']
    lookup_field = 'pk'

    def get_object(self):
        return Problem.objects.get(id=self.kwargs['pk'])


# 연습 문제 / 지역 필터링, 구상 or 즉답형 필터링
class AllPracticeProblemListAPIVIew(ListAPIView):
    serializer_class = ProblemListSerializer
    permission_classes = [IsAuthenticated]
    model = Problem

    def get_queryset(self):
        # 지역 필터링
        regions = Region.objects.all()
        pyeonggawon = regions.get(title='평가원')
        gongtong = regions.get(title='공통')

        region = regions.get(id=int(self.request.query_params.get('region', '1')))

        # 문제 타입 필터링 (구상형, 즉답형, 추가 질문)
        type = self.request.query_params.get('type', 'A')

        # 평가원일 경우
        if region.id == pyeonggawon.id:
            problems = Problem.objects.filter(
                Q(region=region) & Q(type=type) & Q(problem_type='P')
            )

        # 그 외의 경우
        else:
            problems = Problem.objects.filter(
                (Q(region=region) | Q(region=gongtong)) & Q(type=type) & Q(problem_type='P')
            )
        return problems


# 랜덤 연습 문제 / 지역 필터링, 구상 or 즉답형 필터링
class AllRandomPracticeProblemListAPIVIew(ListAPIView):
    serializer_class = ProblemListSerializer
    permission_classes = [IsAuthenticated]
    model = Problem

    def get_queryset(self):
        # 지역 필터링
        regions = Region.objects.all()
        pyeonggawon = regions.get(title='평가원')
        gongtong = regions.get(title='공통')

        region = regions.get(id=int(self.request.query_params.get('region', '1')))

        # 문제 타입 필터링 (구상형, 즉답형, 추가 질문)
        type = self.request.query_params.get('type', 'A')

        # 평가원일 경우
        if region.id == pyeonggawon.id:
            problems = Problem.objects.filter(
                Q(region=region) & Q(type=type) & Q(problem_type='P')
            )

        # 그 외의 경우
        else:
            problems = Problem.objects.filter(
                (Q(region=region) | Q(region=gongtong)) & Q(type=type) & Q(problem_type='P')
            )
        return problems.order_by('?')


# 문제 디테일
class ProblemDetailAPIView(RetrieveAPIView):
    serializer_class = ProblemListSerializer
    permission_classes = [IsAuthenticated]
    queryset = Problem.objects.all().prefetch_related('scrapped_users')
    lookup_field = 'pk'

    def get_object(self):
        return Problem.objects.get(id=self.kwargs['pk'])


# 새로운 기출문제 리스트 (연도별)
class NewRealProblemListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # 지역 필터링 및 기출 출제 지역 가져오기
        regions = Region.objects.all()
        region = regions.get(id=int(self.request.query_params.get('region', '1')))
        real_region = RealRegion.objects.get(title=region.title)
        # 기출 출제 지역 바탕 필터링
        problems = Problem.objects.filter(
            Q(real_region=real_region) & Q(problem_type='A')
        )

        years = list(set(problems.values_list('year', flat=True)))
        years.reverse()
        return_list = []

        for year in years:
            temp_problems = problems.filter(year=year)
            serialized_temp_problems = ProblemListSerializer(data=temp_problems, many=True,
                                                             context={'request': request})
            if serialized_temp_problems.is_valid():
                pass
            serialized_problems = serialized_temp_problems.data
            return_list.append({'year': year, 'problems': serialized_problems})
        return Response(return_list, status=HTTP_200_OK)


# 여기부터 오답노트 리스트
class ScrappedProblemListAPIView(ListAPIView):
    serializer_class = ProblemListSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    model = Problem

    def get_queryset(self):
        big_subject_id = int(self.request.query_params.get('bigSubject', '0'))
        small_subject_id = int(self.request.query_params.get('smallSubject', '0'))
        problems = Problem.objects.prefetch_related('scrapped_users', 'big_subject', 'small_subject')
        # 대주제 전체보기일 경우
        if big_subject_id == 0:
            # ㄹㅇ 전체보기일 경우
            if small_subject_id == 0:
                problem_list = problems.filter(
                    scrapped_users__in=[self.request.user.id]
                )
                return problem_list
            # 소주제만 선택할 경우
            else:
                problem_list = problems.filter(
                    Q(scrapped_users__in=[self.request.user.id]) & Q(small_subject__in=[small_subject_id])
                )
                return problem_list
        else:
            if small_subject_id == 0:
                problem_list = problems.filter(
                    Q(scrapped_users__in=[self.request.user.id]) &
                    Q(big_subject_id=big_subject_id)
                )
                return problem_list
            else:
                problem_list = problems.filter(
                    Q(scrapped_users__in=[self.request.user.id]) &
                    Q(big_subject_id=big_subject_id) &
                    Q(small_subject__in=[small_subject_id])
                )
                return problem_list


# 마이페이지 검색
class SearchProblem(ListAPIView):
    serializer_class = ProblemListSerializer
    permission_classes = [IsAuthenticated]
    model = Problem

    def get_queryset(self):
        number = self.request.query_params.get('number', '  ')
        return Problem.objects.filter(number__startswith=number).order_by('id')


# 실전 모의고사 설명
class TestSetView(RetrieveAPIView):
    serializer_class = TestSetSerializer
    permission_classes = [AllowAny]
    model = TestSet
    lookup_field = 'pk'
    queryset = TestSet.objects.all()

    def get_object(self):
        region = self.kwargs['pk']
        return TestSet.objects.get(region_id=region)


# 실전 모의고사 리스트
class TestSetListView(ListAPIView):
    serializer_class = ProblemListSerializer
    permission_classes = [IsAuthenticated]
    model = Problem

    def get_queryset(self):
        # 지역 필터링
        regions = Region.objects.all()
        seoul = regions.get(title='서울')
        gyeonggi = regions.get(title='경기')
        sejong = regions.get(title='세종')
        pyeonggawon = regions.get(title='평가원')
        gongtong = regions.get(title='공통')
        region = regions.get(id=int(self.request.query_params.get('region', '1')))

        # 공통이거나 특정 지역일 경우 우선 필터링
        if region.id == pyeonggawon.id:
            problems = Problem.objects.filter(region=region)
        else:
            problems = Problem.objects.filter(Q(region=region) | Q(region=gongtong))
        # 서울일 경우
        if region.id == seoul.id:
            # 구상형 3문제, 즉답형 3, 추가 질문 2
            conception = problems.filter(type='A').order_by('?')[:3]
            immediate = problems.filter(type='B').order_by('?')[:3]
            additional = problems.filter(type='C').order_by('?')[:2]
            return conception | immediate | additional
        # 경기일 경우
        elif region.id == gyeonggi.id:
            # 구상형 3문제, 즉답형 2
            conception = problems.filter(type='A').order_by('?')[:3]
            immediate = problems.filter(type='B').order_by('?')[:2]
            return conception | immediate
        # 세종일 경우
        elif region.id == sejong.id:
            # 구상형 3문제, 즉답형 2
            conception = problems.filter(type='A').order_by('?')[:3]
            immediate = problems.filter(type='B').order_by('?')[:2]
            return conception | immediate
        # 평가원일 경우
        else:
            # 구상형 3문제, 즉답형 1
            conception = problems.filter(type='A').order_by('?')[:3]
            immediate = problems.filter(type='B').order_by('?')[:1]
            return conception | immediate
