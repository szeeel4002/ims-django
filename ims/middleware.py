from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # user is not available UNTIL AuthenticationMiddleware
        if not hasattr(request, "user"):
            return self.get_response(request)

        allowed = [
            reverse("login"),
            reverse("signup"),
            reverse("logout"),
        ]

        if request.path.startswith("/admin/"):
            return self.get_response(request)

        if not request.user.is_authenticated and request.path not in allowed:
            return redirect("login")

        return self.get_response(request)
