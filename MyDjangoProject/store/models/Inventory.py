from django.db import models

from .Product import Product

class Inventory(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    last_replenishment = models.DateField()

    def __str__(self):
        return f"Inventory: {self.product}"