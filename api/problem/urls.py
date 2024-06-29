from django.urls import path
from .views import SubjectAPIView, RegionAPIView, PracticeProblemListAPIVIew, RealProblemSetAPIView, \
    RealProblemListAPIVIew, ScrapUpdateAPIView, ScrappedProblemListAPIView, ProblemDetailAPIView

urlpatterns = [
    path('regions/', RegionAPIView.as_view()),
    path('subjects/', SubjectAPIView.as_view()),
    # 연습 문제 리스트
    path('practice-questions/', PracticeProblemListAPIVIew.as_view()),
    # 실전 문제 세트
    path('real-questions-set/', RealProblemSetAPIView.as_view()),
    # 실전 문제 리스트
    path('real-questions/', RealProblemListAPIVIew.as_view()),
    # 오답노트 문제 리스트
    path('scrapped-questions/', ScrappedProblemListAPIView.as_view()),
    # 스크랩 / 해제
    path('update/<int:pk>/', ScrapUpdateAPIView.as_view()),
    # 문제 상세
    path('detail/<int:pk>/', ProblemDetailAPIView.as_view())
]
