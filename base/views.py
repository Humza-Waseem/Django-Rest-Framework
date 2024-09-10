from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.forms.models import model_to_dict

from products.models import Product
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

# Create your views here.
# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all()  #?randomly select one object

#     data = {}

#     if model_data:
#         for items in model_data:
#             data[items.id] = model_to_dict(items)
#         # data = model_to_dict(model_data)   #?converts model data to dictionary
#     # data = {
#     #     'name': 'Hamza',
#     #     'age': 20,
#     #     'is_student': True,
#     #     'is_hostelite':False
#     # }

    
#     return JsonResponse(data)


@api_view(['GET', 'POST'])
def api_home(request, *args, **kwargs):
    model_data = Product.objects.all()  #?randomly select one object

    products = Product.objects.all()
    if (products == None):
        return JsonResponse({'error': 'No products found'})
    else:

        data = ProductSerializer(products, many=True).data  #? to serialize multiple objects we use many=True
    
    return JsonResponse(data, safe=False)














def Home(request):
    # HttpResponse('Hello World')
    return render(request, 'base/home.html')