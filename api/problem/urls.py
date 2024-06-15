from django.urls import path
from api.user.views import UserRegisterView, UserSocialLoginView, UserDetailUpdateView, ProfileDetailUpdateView

urlpatterns = [
    path('social_login/', UserSocialLoginView.as_view()),
    path('email_login/', UserRegisterView.as_view()),
    path('email_signup/', UserRegisterView.as_view()),
    path('profile/', ProfileDetailUpdateView.as_view()),
    path('update/', UserDetailUpdateView.as_view()),
]
