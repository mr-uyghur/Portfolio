from django.urls import path     
from . import views
urlpatterns = [
    path('', views.home),	   
    path('blog/',views.allblogs, name = 'allblogs'),
    path('blog/<int:blog_id>/',views.detail, name = 'detail')
]