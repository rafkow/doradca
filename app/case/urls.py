"""
URL mappings for the case API.
"""
from django.urls import path, include

from case import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('case', views.CaseViewSet)

app_name = 'case'

urlpatterns = [
    path('', include(router.urls)),
]
