from django.db import models
from django.utils import timezone
from inventory.models import Item

class Purchase(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    cost_price = models.FloatField()
    purchase_date = models.DateField(default=timezone.now)
    remaining_qty = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.item.name} - {self.quantity}"

class StockEntry(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    remaining_qty = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.purchase.item.name}: {self.remaining_qty}"
