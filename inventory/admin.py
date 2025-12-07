from django.contrib import admin
from .models import Product, Customer, Supplier

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "quantity", "low_stock_limit", "price")
    list_filter = ("category",)
    search_fields = ("name",)
    list_editable = ("quantity", "low_stock_limit", "price")


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email")
    search_fields = ("name", "phone", "email")


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email")
    search_fields = ("name", "phone", "email")
