from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.add_purchase, name="add_purchase"),
    path("", views.purchase_list, name="purchase_list"),
    path("edit/<int:purchase_id>/", views.edit_purchase, name="edit_purchase"),
    path("delete/<int:purchase_id>/", views.delete_purchase, name="delete_purchase"),
]
