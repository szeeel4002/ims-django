from django.shortcuts import redirect
from django.urls import reverse


class LoginRequiredMiddleware:
    """
    Custom middleware that restricts access to authenticated users only,
    except for public pages like login, signup, admin, and static files.
    """

    def __init__(self, get_response):
        self.get_response = get_response

        # Reverse URLs only for routes that exist
        self.public_paths = set([
            reverse("login"),
            reverse("signup"),
            reverse("admin:login"),
        ])

    def __call__(self, request):

        # 1️⃣ AuthenticationMiddleware MUST run before this middleware
        # so request.user is always available
        user = getattr(request, "user", None)

        # 2️⃣ Allow static/media files (otherwise CSS will break)
        if request.path.startswith("/static/") or request.path.startswith("/media/"):
            return self.get_response(request)

        # 3️⃣ Allow public pages
        if request.path in self.public_paths:
            return self.get_response(request)

        # 4️⃣ If user exists AND is authenticated → allow
        if user and user.is_authenticated:
            return self.get_response(request)

        # 5️⃣ Otherwise redirect to login
        return redirect("login")
