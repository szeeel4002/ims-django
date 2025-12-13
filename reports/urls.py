from django.urls import path
from . import views

urlpatterns = [
    path("", views.report_home, name="reports"),
    path("purchases/", views.purchase_report, name="purchase_report"),
    path("sales/", views.sales_report, name="sales_report"),
    path("stock/", views.stock_report, name="stock_report"),
]
