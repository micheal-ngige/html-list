from django.urls import path
from .views import verify_product, add_product

urlpatterns = [
    path('verify/', verify_product, name='verify_product'),
    path('add/', add_product, name='add_product'),
]
