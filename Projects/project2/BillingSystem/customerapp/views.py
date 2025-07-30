from django.shortcuts import render,HttpResponse , get_object_or_404 ,redirect
from customerapp.models import Customer
# Create your views here.

def home(request):
    return render(request, 'home.html')

def create_customer(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        
        customer = Customer(name=name, email=email, phone=phone, address=address)
        customer.save()
        
        return redirect('create_record', customer_id=customer.id)
    return render(request, 'create_customer.html')

def get_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    return render(request, 'customer_detail.html', {'customer': customer})
