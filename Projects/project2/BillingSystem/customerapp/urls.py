from django.urls import path
from customerapp.views import create_customer, get_customer

urlpatterns = [
    path('create/', create_customer, name='create_customer'),
    path('customer/<int:customer_id>/', get_customer, name='get_customer'),
]