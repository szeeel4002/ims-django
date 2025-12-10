from django.db import models
from inventory.models import Product, Supplier

class Purchase(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def total_amount(self):
        return self.quantity * self.price_per_unit

    def __str__(self):
        return f"{self.product.name} - {self.quantity} units"
