from rest_framework import viewsets
from subject.models.address import Address
from subject.models.subject import Person
from subject.serializers import AddressSerializer, PersonSerializer


class AddressViewset(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class PersonViewset(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


