from django.urls import path
from .views import SubjectAPIView, RegionAPIView, ScrapUpdateAPIView, ScrappedProblemListAPIView, success_view, \
    ProblemDetailAPIView, AllRandomPracticeProblemListAPIVIew, AllPracticeProblemListAPIVIew, upload_excel, \
    NewRealProblemListAPIView, SearchProblem, TestSetView, TestSetListView, ActiveRegionAPIView, MyStudyRoomListAPIView, \
    AllStudyRoomListAPIView, StudyRoomDetailAPIView, StudyRoomSearchAPIView, StudyRoomCreateAPIView, \
    StudyRoomLeaveAPIView

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
    path('active-region/real-questions/', ActiveRegionAPIView.as_view()),
    # 엑셀로 연습문제 업로드
    path('upload-excel/', upload_excel, name='upload_excel'),
    # 성공 페이지
    path('upload-success/', success_view, name='success_page'),

    # 스터디룸 관련

    # 내가 참여한 스터디룸 목록
    path('studyrooms/my/', MyStudyRoomListAPIView.as_view(), name='my-studyroom-list'),
    # 모든 스터디룸 목록
    path('studyrooms/', AllStudyRoomListAPIView.as_view(), name='all-studyroom-list'),
    # 스터디룸 상세 조회 (자동 참여)
    path('studyrooms/<int:pk>/', StudyRoomDetailAPIView.as_view(), name='studyroom-detail'),
    # 방 번호로 스터디룸 검색
    path('studyrooms/search/', StudyRoomSearchAPIView.as_view(), name='studyroom-search'),
    # 스터디룸 생성
    path('studyrooms/create/', StudyRoomCreateAPIView.as_view(), name='studyroom-create'),
    # 스터디룸 나가기
    path('studyrooms/<int:pk>/leave/', StudyRoomLeaveAPIView.as_view(), name='studyroom-leave'),
]
