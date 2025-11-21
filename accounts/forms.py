from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import User
from django.db import models


# --------------------------
# Update Profile Form
# --------------------------
class UserUpdateForm(UserChangeForm):
    password = None  # hide password field on profile edit

    class Meta:
        model = User
        fields = ("username", "email", "phone", "role", "profile_image")


# --------------------------
# Change Password Form
# --------------------------
class CustomPasswordChangeForm(PasswordChangeForm):
    pass


# --------------------------
# Signup Form
# --------------------------
class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    profile_image = models.ImageField(upload_to="profiles/", blank=True, null=True)

    class Meta:
        model = User
        fields = ["username", "email", "profile_image", "password1", "password2"]
