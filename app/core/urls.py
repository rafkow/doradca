from django.urls import path
from core import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="homepage"),
    path("case/", views.case, name="cases"),
]
