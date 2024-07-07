from django.urls import path
from .views import is_deployment_check

urlpatterns = [
    path('', is_deployment_check),
]
