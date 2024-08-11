from django.urls import path
from .views import SubjectAPIView, RegionAPIView, ScrapUpdateAPIView, ScrappedProblemListAPIView, \
    ProblemDetailAPIView, AllRandomPracticeProblemListAPIVIew, AllPracticeProblemListAPIVIew, \
    NewRealProblemListAPIView, SearchProblem, TestSetView, TestSetListView, ActiveRegionAPIView

urlpatterns = [
    path('regions/', RegionAPIView.as_view()),
    path('subjects/', SubjectAPIView.as_view()),
    # 연습 문제 리스트
    path('practice-questions/all/', AllPracticeProblemListAPIVIew.as_view()),
    # 랜덤 연습 문제 리스트
    path('practice-questions/random/all/', AllRandomPracticeProblemListAPIVIew.as_view()),
    # 기출 문제 리스트, 페이지네이션 제외
    path('real-questions/all/', NewRealProblemListAPIView.as_view()),
    # 오답노트 문제 리스트
    path('scrapped-questions/', ScrappedProblemListAPIView.as_view()),
    # 스크랩 / 해제
    path('update/<int:pk>/', ScrapUpdateAPIView.as_view()),
    # 문제 상세
    path('detail/<int:pk>/', ProblemDetailAPIView.as_view()),
    # 마이페이지 검색
    path('mypage/', SearchProblem.as_view()),
    # 실전 모의고사 설명
    path('test-description/<int:pk>/', TestSetView.as_view()),
    path('test/list/', TestSetListView.as_view()),
    # 지역 문제 관련
    path('active-region/real-questions/', ActiveRegionAPIView.as_view())
]
