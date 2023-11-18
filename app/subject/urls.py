"""
URL for subject API
"""
from django.urls import path, include
from subject import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('address', views.AddressViewset)
router.register('pesrson', views.PersonViewset)

app_name = 'subject'

urlpatterns = [
    path('', include(router.urls)),


]
