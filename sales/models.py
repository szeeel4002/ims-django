from django.db import models
from inventory.models import Item

class Sale(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.FloatField()
    selling_price_per_unit = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    # FIFO cost will be computed during sale
    cost_price_total = models.FloatField(default=0)
    profit = models.FloatField(default=0)

    def total_revenue(self):
        return self.quantity * self.selling_price_per_unit

    def __str__(self):
        return f"Sale - {self.item.name}"
