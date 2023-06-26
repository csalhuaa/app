from django.db import models
from django.urls import reverse

from .Category import Category
from .Supplier import Supplier

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images/', default='product_images/default.png')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])
