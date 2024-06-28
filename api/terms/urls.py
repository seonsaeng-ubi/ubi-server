from django.urls import path
from .views import TermsAPIView


urlpatterns = [
    path('list/', TermsAPIView.as_view())
]
