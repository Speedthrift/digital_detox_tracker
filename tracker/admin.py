from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserData
# Register your models here.

class UserDataAdmin(admin.ModelAdmin):
    list_display = ["appname","uid_id","timespent","ondate"]

admin.site.register(UserData, UserDataAdmin)