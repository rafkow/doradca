from rest_framework import viewsets
from case import serializers
from case.models import Case, CaseSubject

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class CaseViewSet(viewsets.ModelViewSet):
    """View od case objects"""
    serializer_class = serializers.CaseDetailsSerializer
    queryset =  Case.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def gat_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.CaseSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        """Case assign user to model"""
        serializer.save(user=self.request.user)


