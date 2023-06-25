from django.shortcuts import render

# Create your views here.

from .models.Category import Category
from .models.Product import Product
from .models.Supplier import Supplier
from .models.Inventory import Inventory
from .models.Order import Order
from .models.OrderItem import OrderItem
from .models.Payment import Payment
from .models.Sale import Sale


def index(request):

    # Generate counts of some of the main objects
    num_products = Product.objects.all().count()

    context = {
        'num_products': num_products,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


from django.views import generic

class ProductListView(generic.ListView):
    model = Product

class ProductDetailView(generic.DetailView):
    model = Product
