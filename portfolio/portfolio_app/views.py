from django.shortcuts import render

# Create your views here.

# def index(request):
#     return HttpResponse("this is the equivalent of @app.route('/')!")
def home(request):
    return render(request, "home.html")
