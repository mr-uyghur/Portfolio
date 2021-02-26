from django.shortcuts import render
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
