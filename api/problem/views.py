from .serializers import BigSubjectSerializer, RegionSerializer, RealProblemSetSerializer, \
    ProblemListSerializer, ProblemUpdateSerializer
from .models import BigSubject, Region, ProblemSet, Problem, SmallSubject
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from ..utils import StandardResultsSetPagination


class SubjectAPIView(ListAPIView):
    serializer_class = BigSubjectSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return BigSubject.objects.all()


class RegionAPIView(ListAPIView):
    serializer_class = RegionSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Region.objects.all()


# 스크랩 취소 / 하기
class ScrapUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = ProblemUpdateSerializer
    queryset = Problem.objects.all()
    allowed_methods = ['put', 'get']
    lookup_field = 'pk'

    def get_object(self):
        return Problem.objects.get(id=self.kwargs['pk'])


# 연습 문제 / 지역 필터링, 구상 or 즉답형 필터링
class PracticeProblemListAPIVIew(ListAPIView):
    serializer_class = ProblemListSerializer
    permission_classes = [AllowAny]
    pagination_class = StandardResultsSetPagination
    model = Problem

    def get_queryset(self):
        region = int(self.request.query_params.get('region', '1'))
        type = self.request.query_params.get('type', 'A')
        random = bool(self.request.query_params.get('random', 'False'))
        problems = Problem.objects.filter(
            region_id=region,
            type=type,
            problem_set__type='P',
        ).prefetch_related('problem_set', 'region')

        if random is True:
            return sorted(list(problems), key=lambda x: hash((self.request.user.id, x.id)))
        else:
            return problems


# 실전 문제셋 (지역별 필터링)
class RealProblemSetAPIView(ListAPIView):
    serializer_class = RealProblemSetSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        region = int(self.request.query_params.get('region', '1'))
        return ProblemSet.objects.filter(
            region_id=region,
            type='A'
        ).prefetch_related('problem_problem_set', 'region')


# 문제 디테일 (지역별 필터링)
class ProblemDetailAPIView(ListAPIView):
    serializer_class = ProblemListSerializer
    permission_classes = [IsAuthenticated]
    queryset = Problem.objects.all().prefetch_related('scrapped_users')
    lookup_field = 'pk'

    def get_object(self):
        return Problem.objects.get(id=self.kwargs['pk'])


# 실전 문제 리스트
class RealProblemListAPIVIew(ListAPIView):
    serializer_class = ProblemListSerializer
    permission_classes = [AllowAny]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        problem_set = int(self.request.query_params.get('set'))
        instance = ProblemSet.objects.get(id=problem_set)
        problems = Problem.objects.filter(
            problem_set=instance
        ).prefetch_related('problem_set')
        return problems


# 여기부터 오답노트 리스트
class ScrappedProblemListAPIView(ListAPIView):
    serializer_class = ProblemListSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    model = Problem

    def get_queryset(self):
        big_subject_id = int(self.request.query_params.get('big_subject', '0'))
        small_subject_id = int(self.request.query_params.get('small_subject', '0'))
        problems = Problem.objects.all().prefetch_related('scrapped_users', 'small_subject', 'big_subject')
        if big_subject_id == 0:
            problem_list = problems.filter(
                scrapped_users__in=[self.request.user.id]
            )
            return problem_list
        else:
            if small_subject_id == 0:
                problem_list = problems.filter(
                    scrapped_users__in=[self.request.user.id],
                    big_subject_id=big_subject_id
                )
                return problem_list
            else:
                problem_list = problems.filter(
                    scrapped_users__in=[self.request.user.id],
                    small_subject__in=[small_subject_id]
                )
                return problem_list
