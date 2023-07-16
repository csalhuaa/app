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


from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class ProductCreate(PermissionRequiredMixin, CreateView):
    model = Product
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'

class ProductUpdate(PermissionRequiredMixin, UpdateView):
    model = Product
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'

class ProductDelete(PermissionRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('products')
    permission_required = 'catalog.can_mark_returned'


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]