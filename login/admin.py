from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from login.models import Login

# Register your models here.
class LoginAdmin(admin.ModelAdmin):
    list_display = ('username','password')

admin.site.register(Login, LoginAdmin)