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

        # ensure request.user exists
        user = getattr(request, 'user', None)

        # Allow access if user object missing (first middleware stage)
        if user is None:
            return self.get_response(request)

        # Allow authenticated users
        if user.is_authenticated:
            return self.get_response(request)

        # Allow public URLs
        if request.path in self.public_paths:
            return self.get_response(request)

        return redirect('login')
