from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def create_person(request):
    return HttpResponse("hello darknes my old friend")