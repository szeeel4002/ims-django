from django.db import models

from django.db import models
from django.utils import timezone

class Item(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name



class Purchase(models.Model):
    item_name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    cost_price = models.FloatField()
    purchase_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.item_name} - {self.quantity}"


class StockEntry(models.Model):
    """
    Each purchase becomes a stock entry.
    FIFO means sales will consume the OLDEST StockEntry first.
    """
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    remaining_qty = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.purchase.item_name}: {self.remaining_qty}"


class Sale(models.Model):
    item_name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    sale_price = models.FloatField()
    sale_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.item_name} - {self.quantity}"

    # FIFO LOGIC HERE
    def save(self, *args, **kwargs):
        """
        When a sale is made:
            1. Find all stock entries for this item (oldest first)
            2. Reduce stock using FIFO
            3. If not enough stock → raise error
        """
        qty_to_reduce = self.quantity

        stock_entries = StockEntry.objects.filter(
            purchase__item_name=self.item_name,
            remaining_qty__gt=0
        ).order_by("purchase__purchase_date")  # oldest first

        for entry in stock_entries:
            if qty_to_reduce == 0:
                break

            if entry.remaining_qty >= qty_to_reduce:
                entry.remaining_qty -= qty_to_reduce
                entry.save()
                qty_to_reduce = 0
            else:
                qty_to_reduce -= entry.remaining_qty
                entry.remaining_qty = 0
                entry.save()

        if qty_to_reduce > 0:
            raise ValueError("Not enough stock available to complete this sale.")

        super().save(*args, **kwargs)
