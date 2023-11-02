from django.shortcuts import render
from product.serializers import ProductSerializer
from product.models import Product

from rest_framework.views import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def product(request):
    instance = Product.objects.all().order_by('?').first()
    data = {}
    if instance:
        data = ProductSerializer(instance).data
    
    return Response(data)