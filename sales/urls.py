from django.urls import path
from . import views

urlpatterns = [
    path("", views.sales_list, name="sales_list"),
    path("add/", views.add_sale, name="add_sale"),
    path("edit/<int:sale_id>/", views.edit_sale, name="edit_sale"),
    path("delete/<int:sale_id>/", views.delete_sale, name="delete_sale"),
    path("invoice/<int:sale_id>/", views.sale_invoice, name="sale_invoice"),
]
