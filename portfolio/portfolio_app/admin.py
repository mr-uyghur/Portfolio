from django.contrib import admin

from .models import *

# Register your models here.


#code for showing model in the admin page as super user
admin.site.register(Job)
admin.site.register(Blog)
