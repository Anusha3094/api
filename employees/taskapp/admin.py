# from django.contrib import admin
# from .models import *

# # Register your models here.
# admin.site.register(Role)
from django.contrib import admin
from .models import Employee, Comment,Role

admin.site.register(Employee)
admin.site.register(Comment)
admin.site.register(Role)