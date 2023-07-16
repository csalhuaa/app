from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),
    path('categorys/', views.CategoryListView.as_view(), name='categorys'),
    path('category/<int:pk>', views.CategoryDetailView.as_view(), name='category_detail'),
    path('product/create/', views.ProductCreate.as_view(), name='product_create'),
    path('product/<int:pk>/update/', views.ProductUpdate.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', views.ProductDelete.as_view(), name='product_delete'),
    path('accounts/register/', views.register, name='register'),
]