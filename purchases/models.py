from django.db import models
from django.utils import timezone

class Purchase(models.Model):
    item_name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    cost_price = models.FloatField()
    purchase_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.item_name} - {self.quantity}"
