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


class SignupForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Username'}),
        help_text=''   # remove default help text
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email Address'}),
        required=True
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
        help_text=''   # remove password help text too
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        help_text=''
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
