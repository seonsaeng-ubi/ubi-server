from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK
from .models import Setting


@api_view(['GET'])
def is_deployment_check(request):
    is_deployment_model = Setting.objects.last()
    return Response({'version': is_deployment_model.version}, status=HTTP_200_OK)
