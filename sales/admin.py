from django.contrib import admin
from .models import Sale

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "quantity",
        "selling_price",
        "cost_price",
        "profit",
        "created_at",
    )
