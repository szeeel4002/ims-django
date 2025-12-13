from django.urls import path
from . import views

urlpatterns = [
    path("stock/", views.stock_report, name="stock_report"),
    path("purchases/", views.purchase_report, name="purchase_report"),
    path("fifo/", views.fifo_report, name="fifo_report"),
]
