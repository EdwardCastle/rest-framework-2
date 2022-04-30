from products.models import Product
from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by('?').first()
    print(model_data)
    data = {}
    if model_data:
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price
    return JsonResponse(data)