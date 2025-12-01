from django.urls import path
from . import views

urlpatterns = [
    path("", views.sales_home, name="sales_home"),
    path("add/", views.add_sale, name="add_sale"),
]

