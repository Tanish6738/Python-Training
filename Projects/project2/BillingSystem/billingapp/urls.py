from django.urls import path
from billingapp.views import create_record, view_records

urlpatterns = [
    path('create/', create_record, name='create_record'),
    path('create/<int:customer_id>/', create_record, name='create_record'),
    path('view/<int:record_id>/', view_records, name='view_records'),
]