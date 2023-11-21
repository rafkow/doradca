from rest_framework import serializers
from case.models import Case, CaseSubject


class CaseSerializer(serializers.ModelSerializer):
    """Serializer for case objects"""

    class Meta:
        model = Case
        fields = ['id', 'signature', 'type']
        read_only_fields = ['id']


class CaseDetailsSerializer(CaseSerializer):
    """ Exten of Case Serializer"""

    class Meta(CaseSerializer.Meta):
        fields = CaseSerializer.Meta.fields + ['description']



