from django.contrib import admin
from .models import User   # <-- FIXED

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "phone", "role")
