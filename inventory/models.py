from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    category = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
