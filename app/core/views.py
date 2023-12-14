from django.shortcuts import render
from case.models import Case



def index(request):
    return render(request, 'index.html')

def case(request):
    context = {
        'cases': Case.objects.all()
    }
    return render(request, 'case/list.html', context)
