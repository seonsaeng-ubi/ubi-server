from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.user.views import UserSocialLoginView, ProfileDetailUpdateView, UserRegisterView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('social-login/', UserSocialLoginView.as_view()),
    path('email-login/', UserRegisterView.as_view()),
    path('email-signup/', UserRegisterView.as_view()),
    path('profile/', ProfileDetailUpdateView.as_view()),
]
