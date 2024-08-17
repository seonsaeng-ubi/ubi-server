from django.urls import path
from .views import is_deployment_check, personal_info_html_view, service_agreement_html_view, marketing_agreement_html_view

urlpatterns = [
    path('', is_deployment_check),
    path('personal-info-agreement/', personal_info_html_view),
    path('service-agreement/', service_agreement_html_view),
    path('marketing-agreement/', marketing_agreement_html_view),
]
