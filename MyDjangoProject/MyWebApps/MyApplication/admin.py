from django.contrib import admin

# Register your models here.
from .models.Category import Category
from .models.Product import Product
from .models.Supplier import Supplier
from .models.Inventory import Inventory
from .models.Order import Order
from .models.OrderItem import OrderItem
from .models.Payment import Payment
from .models.Sale import Sale

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(Inventory)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)
admin.site.register(Sale)