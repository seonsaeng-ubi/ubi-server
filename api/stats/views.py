from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK
from .models import Setting


@api_view(['GET'])
def is_deployment_check(request):
    is_deployment_model = Setting.objects.first().setting
    result = False if is_deployment_model == 'A' else True
    return Response({'results': result}, status=HTTP_200_OK)
