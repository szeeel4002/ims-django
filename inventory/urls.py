from django.urls import path
from . import views

urlpatterns = [
    # Dashboard / Home
    path("", views.dashboard, name="dashboard"),

    # Products
    path("products/", views.product_list, name="product_list"),
    path("products/add/", views.product_create, name="product_create"),
    path("products/<int:pk>/edit/", views.product_edit, name="product_edit"),
    path("products/<int:pk>/delete/", views.product_delete, name="product_delete"),

    # Suppliers
    path("suppliers/", views.supplier_list, name="supplier_list"),
    path("suppliers/add/", views.supplier_create, name="supplier_create"),
    path("suppliers/<int:pk>/edit/", views.supplier_edit, name="supplier_edit"),
    path("suppliers/<int:pk>/delete/", views.supplier_delete, name="supplier_delete"),

    # Customers
    path("customers/", views.customer_list, name="customer_list"),
    path("customers/add/", views.customer_create, name="customer_create"),
    path("customers/<int:pk>/edit/", views.customer_edit, name="customer_edit"),
    path("customers/<int:pk>/delete/", views.customer_delete, name="customer_delete"),
]
