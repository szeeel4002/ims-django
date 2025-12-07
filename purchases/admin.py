from django.contrib import admin
from .models import Purchase

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ("date", "product", "supplier", "quantity", "total_price")
    list_filter = ("date", "supplier")
    search_fields = ("product__name", "supplier__name")
