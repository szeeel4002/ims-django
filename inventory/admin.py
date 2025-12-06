from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "quantity", "price", "category")
    list_filter = ("category",)
    search_fields = ("name", "category")

admin.site.register(Product, ProductAdmin)
