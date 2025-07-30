from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from billingapp.models import BillingRecord
from customerapp.models import Customer
import json

# Create your views here.

def create_record(request, customer_id=None):
    customer = None
    if customer_id:
        customer = get_object_or_404(Customer, id=customer_id)
    
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        if customer:
            customer_name = customer.name
        
        # Get product data from form
        product_names = request.POST.getlist('product_name')
        product_prices = request.POST.getlist('product_price')
        product_quantities = request.POST.getlist('product_quantity')
        
        # Create product list
        product_list = []
        total_amount = 0
        
        for i in range(len(product_names)):
            if product_names[i] and product_prices[i] and product_quantities[i]:
                price = float(product_prices[i])
                quantity = int(product_quantities[i])
                subtotal = price * quantity
                
                product_list.append({
                    'name': product_names[i],
                    'price': price,
                    'quantity': quantity,
                    'subtotal': subtotal
                })
                total_amount += subtotal
        
        billing_record = BillingRecord(
            customer_name=customer_name,
            product_list=product_list,
            total_amount=total_amount
        )
        billing_record.save()
        
        return redirect('view_records', record_id=billing_record.id)
    
    return render(request, 'create_billing_record.html', {'customer': customer})

def view_records(request, record_id):
    billing_record = get_object_or_404(BillingRecord, id=record_id)
    return render(request, 'view_billing_record.html', {'billing_record': billing_record})
