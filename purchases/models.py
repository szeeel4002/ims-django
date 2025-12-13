from django.db import models
from inventory.models import Product

class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price_per_unit = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
