from django.urls import path
from . import views

urlpatterns = [
    path("purchases/", views.purchase_report, name="purchase_report"),
    path("sales/", views.sales_report, name="sales_report"),
    path("stock/", views.stock_report, name="stock_report"),
]
