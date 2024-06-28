from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from .serializers import TermsSerializer
from .models import Terms


class TermsAPIView(ListAPIView):
    serializer_class = TermsSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Terms.objects.all()
