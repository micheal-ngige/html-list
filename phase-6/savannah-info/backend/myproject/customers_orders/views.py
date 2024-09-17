import africastalking
from rest_framework import viewsets
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer
from .utils import key,name


def send_sms(to, message):
    username = name
    api_key = key
    africastalking.initialize(username, api_key)
    sms = africastalking.SMS
    response = sms.send(message, [to])
    return response

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        order = serializer.save()
        customer = order.customer
        message = f"New order placed: {order.item} for {order.amount}"
        send_sms(customer.phone_number, message)
