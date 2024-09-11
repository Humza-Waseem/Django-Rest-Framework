from django.contrib import admin
from django.urls import path, include
from . import views
from .views import  Home,api_home
urlpatterns = [
    path('', Home, name='home'),
    path('api/', api_home, name = 'api'),
    
    # path('products/', ProductList.as_view(), name='product-list')
     
]
