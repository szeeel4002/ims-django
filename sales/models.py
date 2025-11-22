from django.db import models
from django.utils import timezone
from inventory.models import Item

class Sale(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    sale_price = models.FloatField()
    sale_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.item.name} - {self.quantity}"
