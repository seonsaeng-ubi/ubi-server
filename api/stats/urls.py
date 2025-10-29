from django.urls import path
from .views import is_deployment_check, personal_info_html_view, service_agreement_html_view, \
    marketing_agreement_html_view, is_android_deployment_check

urlpatterns = [
    path('', is_deployment_check),
    path('android/', is_android_deployment_check),
    path('personal-info-agreement/', personal_info_html_view),
    path('service-agreement/', service_agreement_html_view),
    path('marketing-agreement/', marketing_agreement_html_view),
]
