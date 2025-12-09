from django.contrib import admin
from .models import Product, Supplier, Customer


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "stock", "price")
    search_fields = ("name", "category")


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "phone")
    search_fields = ("name", "email")


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "phone")
    search_fields = ("name", "email")
