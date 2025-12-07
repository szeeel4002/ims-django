from django.urls import path
from . import views

urlpatterns = [
    path("sales-report/", views.sales_report, name="sales_report"),
    path("purchase-report/", views.purchase_report, name="purchase_report"),
]
