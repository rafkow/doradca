from django.urls import path, include
from subject import views, api
from rest_framework import routers

router = routers.DefaultRouter()
router.register('address', api.AddressViewset)


urlpatterns = [
    path('', include(router.urls)),
    path('api/', api.getData ),
    path('api/add', api.addAddress ),
]
