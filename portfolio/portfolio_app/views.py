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

def allblogs(request):
    blogs = Blog.objects
    context = {
        'blogs':blogs
    }
    return render(request,"allblogs.html",context)

def detail(request, blog_id):
    detail_blog = get_object_or_404(Blog, pk = blog_id) #pk = primary key
    context = {
        'blog':detail_blog
    }
    return render(request, "detail.html",context)
    

