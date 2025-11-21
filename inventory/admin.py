from django.contrib import admin
from inventory.models import Item, StockEntry
from purchases.models import Purchase

admin.site.register(Item)
admin.site.register(StockEntry)
admin.site.register(Purchase)
