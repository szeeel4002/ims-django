from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class AuthTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.signup_url = reverse("signup")
        self.login_url = reverse("login")
        self.dashboard_url = reverse("dashboard")

        # Create test user
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="TestPass123"
        )

    def test_signup_page_loads(self):
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/signup.html")

    def test_user_can_signup(self):
        data = {
            "username": "newuser",
            "email": "new@example.com",
            "password1": "TestPass123",
            "password2": "TestPass123"
        }
        response = self.client.post(self.signup_url, data)
        self.assertEqual(User.objects.count(), 2)  # user created
        self.assertEqual(response.status_code, 302)  # redirect to login

    def test_login_page_loads(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/login.html")

    def test_user_can_login(self):
        login_success = self.client.login(
            username="testuser",
            password="TestPass123"
        )
        self.assertTrue(login_success)

    def test_dashboard_requires_login(self):
        response = self.client.get(self.dashboard_url)
        # Should redirect to login page
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith("/accounts/login/"))

    def test_dashboard_access_after_login(self):
        self.client.login(username="testuser", password="TestPass123")
        response = self.client.get(self.dashboard_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/dashboard.html")
