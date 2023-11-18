from rest_framework import viewsets
from case import serializers
from case.models import Case, CaseSubject

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class CaseViewSet(viewsets.ModelViewSet):
    """View od case objects"""
    serializer_class = serializers.CaseSerializer
    queryset =  Case.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


