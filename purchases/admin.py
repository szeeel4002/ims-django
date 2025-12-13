from django.contrib import admin
from .models import Purchase

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ("product", "quantity", "price_per_unit", "created_at")
    list_filter = ("product",)
