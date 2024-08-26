from django.http import JsonResponse
from .models import Product
from django.views.decorators.csrf import csrf_exempt
import json

def verify_product(request):
    product_code = request.GET.get('code')
    try:
        product = Product.objects.get(code=product_code)
        response = {
            "status": product.status,
            "message": product.message,
            "timestamp": product.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        }
    except Product.DoesNotExist:
        response = {
            "status": "unknown",
            "message": "Product not found.",
            "timestamp": ""
        }
    return JsonResponse(response)




@csrf_exempt
def add_product(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            code = data['code']
            status = data['status']
            message = data['message']

            # Create and save the new product
            product = Product.objects.create(code=code, status=status, message=message)
            product.save()

            response = {
                "success": True,
                "message": "Product added successfully.",
                "product_id": product.id
            }
        except KeyError:
            response = {
                "success": False,
                "message": "Invalid data provided."
            }
    else:
        response = {
            "success": False,
            "message": "Invalid request method."
        }

    return JsonResponse(response)
