from rest_framework import serializers
from case.models import Case, CaseSubject


class CaseSerializer(serializers.ModelSerializer):
    """Serializer for case objects"""

    class Meta:
        model = Case
        fields = ['id', 'signature', 'type', 'description']
        read_only_fields = ['id']





