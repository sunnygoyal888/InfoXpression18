from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'title' : 'Home',
    }
    return render(request, 'common/home.html', context)