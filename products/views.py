from django.shortcuts import render
from .models import Product
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProductSerializer
from .models import Product
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import JsonResponse
from rest_framework import generics




# Create your views here.


@api_view(['GET', 'POST'])
def api_home(request, *args, **kwargs):
    model_data = Product.objects.all()  #?randomly select one object

    products = Product.objects.all()
    if (products == None):
        return JsonResponse({'error': 'No products found'})
    else:
        data = ProductSerializer(products, many=True).data  #? to serialize multiple objects we use many=True
    
    return JsonResponse(data, safe=False)



#  using this view to get the list of products as a json response api 
class ProductList(APIView):   # this is our api view 
    
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class ProductDetailsAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all() #* this is the query set that we want to retrieve from the database
    serializer_class = ProductSerializer  #? this is the serializer class that we want to use to serialize the data
    lookup_field = 'id' #? this is the field that we want to use to look up the object in the database. This is mandatory to use this field in the url path to get the object from the database otherwise the object will not be found and it will return a 404 error.

class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# class ProductUpdateView(generics.UpdateAPIView):
#     queryset = Product.objects.all()
#     serializer
#     class = ProductSerializer
#     lookup_field = 'id'
#     lookup_url_kwarg = 'id'
#     def update(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#     def partial_update(self, request, *args, **kwargs):
#         return self.partial_update(request, *args, **kwargs)

# class ProductDeleteView(generics.DestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = 'id'
#     # lookup_url_kwarg = 'id'
    