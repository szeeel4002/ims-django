from django.contrib import admin
from .models import Sale

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ("customer", "product", "quantity", "price_per_unit", "date")
    search_fields = ("customer__name", "product__name")
    list_filter = ("customer", "product")
