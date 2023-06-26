from django.shortcuts import render

from django.views.generic import ListView
from .forms import ProductFilterForm

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
'''
class ProductListView(generic.ListView):
    model = Product
'''
class ProductListView(ListView):
    model = Product
    template_name = 'store/products.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        form = ProductFilterForm(self.request.GET)

        if form.is_valid():
            name = form.cleaned_data['name']
            min_price = form.cleaned_data['min_price']
            max_price = form.cleaned_data['max_price']
            category = form.cleaned_data['category']

            # Aplica los filtros a la consulta
            if name:
                queryset = queryset.filter(name__icontains=name)
            if min_price:
                queryset = queryset.filter(price__gte=min_price)
            if max_price:
                queryset = queryset.filter(price__lte=max_price)
            if category:
                queryset = queryset.filter(category=category)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ProductDetailView(generic.DetailView):
    model = Product


class CategoryListView(generic.ListView):
    model = Category

class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = 'store/category_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.get_object()
        context['products'] = category.product_set.all()  # Obtiene todos los productos relacionados con la categoría
        return context
    