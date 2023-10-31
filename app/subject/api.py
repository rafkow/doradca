from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from subject.models.address import Address
from subject.serializers.address import AddressSerializer


@api_view(['GET'])
def getData(request):
    addresses = Address.objects.all()
    serializer = AddressSerializer(addresses, many=True)
    return Response(serializer.data)


class AddressViewset(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


@api_view(['POST'])
def addAddress(request):
    serializer = AddressSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)