from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.forms.models import model_to_dict

from products.models import Product

# Create your views here.
def api_home(request, *args, **kwargs):
    model_data = Product.objects.all()  #!randomly select one object

    data = {}

    if model_data:
        for items in model_data:
            data[items.id] = model_to_dict(items)
        # data = model_to_dict(model_data)   #!converts model data to dictionary
    # data = {
    #     'name': 'Hamza',
    #     'age': 20,
    #     'is_student': True,
    #     'is_hostelite':False
    # }

    
    return JsonResponse(data)



def Home(request):
    # HttpResponse('Hello World')
    return render(request, 'base/home.html')