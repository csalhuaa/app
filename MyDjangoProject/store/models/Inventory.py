from django.db import models

from .Product import Product

class Inventory(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    last_replenishment = models.DateField()
    total_sold = models.PositiveIntegerField(default=0)
    total_purchased = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Inventory: {self.product}"

    def increase_quantity(self, amount):
        self.product.quantity += amount
        self.total_purchased += amount
        self.product.save()
        self.save()

    def decrease_quantity(self, amount):
        if self.product.quantity >= amount:
            self.product.quantity -= amount
            self.total_sold += amount
            self.product.save()
            self.save()
        else:
            raise ValueError('Cantidad insuficiente en el inventario.')

    def get_available_quantity(self):
        return self.product.quantity - self.total_sold

    def get_sold_quantity(self):
        return self.total_sold

    def get_purchased_quantity(self):
        return self.total_purchased

    def get_total_quantity(self):
        return self.product.quantity

    def get_inventory_value(self):
        return self.product.price * self.product.quantity
