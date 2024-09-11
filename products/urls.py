from django.contrib import admin
from django.urls import path, include
from . import views
from .views import   ProductList
from .views import api_home

urlpatterns= [
    path('', views.api_home, name='home'),
    path('products/', ProductList.as_view(), name='product-list')
]