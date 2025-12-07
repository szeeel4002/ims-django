from django.urls import path
from . import views

urlpatterns = [
    # ... existing product urls ...

    path("customers/", views.customer_list, name="customer_list"),
    path("customers/add/", views.add_customer, name="add_customer"),
    path("customers/edit/<int:customer_id>/", views.edit_customer, name="edit_customer"),
    path("customers/delete/<int:customer_id>/", views.delete_customer, name="delete_customer"),

    path("suppliers/", views.supplier_list, name="supplier_list"),
    path("suppliers/add/", views.add_supplier, name="add_supplier"),
    path("suppliers/edit/<int:supplier_id>/", views.edit_supplier, name="edit_supplier"),
    path("suppliers/delete/<int:supplier_id>/", views.delete_supplier, name="delete_supplier"),
]
