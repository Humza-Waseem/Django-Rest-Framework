from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.
def api_home(request, *args, **kwargs):
    data = {
        'name': 'Hamza',
        'age': 20
    }
    return JsonResponse(data)
def Home(request):
    # HttpResponse('Hello World')
    return render(request, 'base/home.html')