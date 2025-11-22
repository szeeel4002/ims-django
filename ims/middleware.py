from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        self.public_paths = [
            reverse('login'),
            reverse('signup'),
        ]

    def __call__(self, request):

        # FIRST check that request has user (AuthenticationMiddleware adds it)
        if not hasattr(request, "user"):
            return self.get_response(request)

        # allow logged-in users
        if request.user.is_authenticated:
            return self.get_response(request)

        # allow public pages
        if request.path in self.public_paths:
            return self.get_response(request)

        # redirect all other requests
        return redirect('login')
