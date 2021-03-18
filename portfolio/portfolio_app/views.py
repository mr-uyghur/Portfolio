from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.

# def index(request):
#     return HttpResponse("this is the equivalent of @app.route('/')!")
def home(request):
    jobs = Job.objects
    context = {
        'jobs': jobs
    }
    return render(request, "home.html",context)




def test(request):
    return render(request,'test/index.html')

def projects(request):
    jobs = Job.objects
    context = {
        'jobs': jobs
    }
    return render(request, 'test/works.html',context)

def about(request):
    return render(request,'test/about.html')
    

