from rest_framework.decorators import api_view

from products.models import Product
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import decorators

from products.serializers import ProductSerializer


@api_view(['POST'])
def api_home(request, *args, **kwargs):
    request = Product.objects.all().first()
    product = {}
    if request:
        product = ProductSerializer(request)
    return Response(product.data)
