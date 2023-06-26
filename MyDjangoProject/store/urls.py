from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),
    path('categorys/', views.CategoryListView.as_view(), name='categorys'),
    path('category/<int:pk>', views.CategoryDetailView.as_view(), name='category_detail'),
]