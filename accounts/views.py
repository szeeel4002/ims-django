from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

from .forms import SignupForm, UserUpdateForm, CustomPasswordChangeForm


# --------------------------
# SIGNUP VIEW
# --------------------------
def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! Please log in.")
            return redirect("login")
    else:
        form = SignupForm()

    return render(request, "accounts/signup.html", {"form": form})


# --------------------------
# LOGIN VIEW
# --------------------------
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Save session data
            request.session["last_login_time"] = str(timezone.now())

            return redirect("home")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "accounts/login.html")


# --------------------------
# LOGOUT VIEW
# --------------------------
def logout_view(request):
    logout(request)
    messages.success(request, "You have logged out.")
    return redirect("login")


# --------------------------
# DASHBOARD VIEW
# --------------------------
@login_required
def dashboard_view(request):
    return render(request, "accounts/dashboard.html")


# --------------------------
# PROFILE VIEW
# --------------------------
@login_required
def profile_view(request):
    return render(request, "accounts/profile.html")


# --------------------------
# PROFILE EDIT VIEW
# --------------------------
@login_required
def profile_edit(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("profile")
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, "accounts/profile_edit.html", {"form": form})


# --------------------------
# CHANGE PASSWORD VIEW
# --------------------------
@login_required
def change_password(request):
    if request.method == "POST":
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # keep user logged in
            messages.success(request, "Password updated successfully.")
            return redirect("profile")
    else:
        form = CustomPasswordChangeForm(user=request.user)

    return render(request, "accounts/change_password.html", {"form": form})
