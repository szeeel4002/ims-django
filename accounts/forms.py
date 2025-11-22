from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import User
from django.db import models

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"})
    )



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


class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get("password")
        p2 = cleaned_data.get("confirm_password")

        if p1 != p2:
            raise forms.ValidationError("Passwords do not match!")

        return cleaned_data

