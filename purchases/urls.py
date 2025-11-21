from django.urls import path
from .views import add_purchase

urlpatterns = [
    path("add/", add_purchase, name="add_purchase"),
]
