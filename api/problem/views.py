from .serializers import BigSubjectSerializer, RegionSerializer, RealProblemSetSerializer, ProblemListSerializer, \
    ProblemUpdateSerializer
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import SmallSubject, BigSubject, Region, ProblemSet, Problem
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
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        region = self.request.query_params.get('region', '1')
        type = self.request.query_params.get('type', 'A')
        problems = Problem.objects.filter(
            region=region,
            type=type,
            problem_set_type='P',
        )
        return problems


# 실전 문제셋  (지역별 필터링)
class RealProblemSetAPIView(ListAPIView):
    serializer_class = RealProblemSetSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        region = self.request.query_params.get('region', '1')
        return ProblemSet.objects.filter(
            region=region,
            type='A'
        )


# 실전 문제 리스트
class RealProblemListAPIVIew(ListAPIView):
    serializer_class = ProblemListSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        problem_set = self.request.query_params.get('problem_set', '1')
        problems = Problem.objects.filter(
            problem_set_id=problem_set
        )
        return problems


# 여기부터 오답노트 리스트
class ScrappedProblemListAPIView(ListAPIView):
    serializer_class = ProblemListSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        big_subject = self.request.query_params.get('big_subject', '0')
        small_subject = self.request.query_params.get('small_subject', '0')
        if big_subject == 0:
            problems = Problem.objects.filter(
                scrapped_users__in=self.request.user
            )
            return problems
        else:
            if small_subject == 0:
                problems = Problem.objects.filter(
                    scrapped_users__in=self.request.user,
                    big_subject_id=big_subject
                )
                return problems
            else:
                problems = Problem.objects.filter(
                    scrapped_users__in=self.request.user,
                    small_subject__in=small_subject
                )
                return problems
