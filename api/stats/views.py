from .static import marketing_agreement, personal_info, service_agreement
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from .models import Setting


@api_view(['GET'])
def is_deployment_check(request):
    is_deployment_model = Setting.objects.last()
    return Response({'version': is_deployment_model.version}, status=HTTP_200_OK)


@api_view(['GET'])
@renderer_classes([StaticHTMLRenderer])
def service_agreement_html_view(request):
    data = service_agreement.data
    return Response(data)


@api_view(['GET'])
@renderer_classes([StaticHTMLRenderer])
def personal_info_html_view(request):
    data = personal_info.data
    return Response(data)


@api_view(['GET'])
@renderer_classes([StaticHTMLRenderer])
def marketing_agreement_html_view(request):
    data = marketing_agreement.data
    return Response(data)
