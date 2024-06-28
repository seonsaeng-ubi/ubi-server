from rest_framework.serializers import ModelSerializer
from .models import Terms


class TermsSerializer(ModelSerializer):
    class Meta:
        model = Terms
        fields = ['id', 'title', 'small_subject']
