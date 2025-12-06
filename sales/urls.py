from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.sale_list, name="sale_list"),
    path('add/', views.add_sale, name="add_sale"),
    path('invoice/<int:sale_id>/', views.generate_invoice, name="generate_invoice"),
]
