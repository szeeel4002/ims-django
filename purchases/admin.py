from django.contrib import admin
from .models import Purchase

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ("supplier", "product", "quantity", "price_per_unit", "created_at")
    search_fields = ("supplier__name", "product__name")
    list_filter = ("supplier", "product")
