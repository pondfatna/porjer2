# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'autname', 'sex', 'age', 'live', 'is_staff')
    search_fields = ('username', 'email', 'autname')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Product)