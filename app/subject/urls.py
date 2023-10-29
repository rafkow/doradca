from django.urls import path
from subject import views


urlpatterns = [
    path('', views.create_person, name='index')
]
