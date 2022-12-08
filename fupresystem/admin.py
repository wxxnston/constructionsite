from django.contrib import admin
from .models import *
# Register your models here.
class showresponse(admin.ModelAdmin):
    list_display=('firstname','lastname','address','phone','company')
admin.site.register(response,showresponse)

class showlogin(admin.ModelAdmin):
    list_display=('username','password')
admin.site.register(login,showlogin)