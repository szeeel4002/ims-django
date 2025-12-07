from django.contrib import admin
from .models import Sale

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ("date", "product", "customer", "quantity", "total_price")
    list_filter = ("date", "customer")
    search_fields = ("product__name", "customer__name")
