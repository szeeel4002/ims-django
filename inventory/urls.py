from django.urls import path
from . import views
from django.urls import path
from .views import home, product_list

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path("", home, name="home"),
    path("products/", product_list, name="product_list"),

    # Products
    path('products/', views.product_list, name='product_list'),
    path('products/add/', views.add_product, name='add_product'),
    path("add/", views.add_product, name="add_product"),

    # Customers
    path('customers/', views.customer_list, name='customer_list'),

    # Suppliers
    path('suppliers/', views.supplier_list, name='supplier_list'),

    # Purchases
    path('purchases/', views.purchase_list, name='purchase_list'),

    # Sales
    path('sales/', views.sales_list, name='sales_list'),

    # Reports
    path('report/purchase/', views.purchase_report, name='purchase_report'),
    path('report/sales/', views.sales_report, name='sales_report'),
    path('report/stock/', views.stock_report, name='stock_report'),
    path("", home, name="home"),
    path("products/", product_list, name="product_list"),
]
