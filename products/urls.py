from django.contrib import admin
from django.urls import path, include
from . import views
from .views import   ProductList,ProductDetailsAPIView,ProductCreateView
from .views import api_home

urlpatterns= [
    path('', views.api_home, name='home'),
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:id>/', ProductDetailsAPIView.as_view(), name='product-details'),
    path('products/Create', ProductCreateView.as_view(), name='product-create'),
    # path('products/delete/<int:id>', ProductDeleteView.as_view(), name='product-delete'),

        
]