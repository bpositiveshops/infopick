from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse
from django.utils import timezone
from .models import *
from django.shortcuts import get_object_or_404
# Create your views here.

def customer_list(request):
    # Retrieve the list of customers from the database
    customer_list = Customer.objects.all()
    # Render the customer_list.html template with the customer_list context variable
    return render(request, 'customer_app/customer_list.html', {'customer_list': customer_list})

def add_customer(request, client_id):
    if request.method == 'POST':
        custname = request.POST.get('custname')
        email =  request.POST.get('custemail')
        phone = request.POST.get('custphone')
        created_date = timezone.now()  # Use Django's timezone-aware datetime
        last_updated = None  # Assuming no update yet

        # Filter clientinfo
        client_info_queryset = ClientInfo.objects.filter(email=request.user, clientid=client_id)

        # Assuming there should be only one ClientInfo instance matching the filter criteria
        client_info_instance = get_object_or_404(client_info_queryset)

        # Create a new Customer instance
        new_customer = Customer(
            custname=custname,
            email=email,
            phone=phone,
            client_info=client_info_instance,  # Assuming clientid is the ID of the associated Client
            created_date=created_date,
            last_updated=last_updated
        )
        # Save the new customer to the database
        new_customer.save()
        return  JsonResponse({'message': 'Customer created successfully'}) 
     # Render the addcustomer page
    return render(request, 'customer_app/addcustomer.html', {'client_id': client_id})

def customer_pay(request, client_id):
    # Generate the URL using reverse
    url = reverse('customer_pagelink', kwargs={'client_id': client_id})
     # Render the addcustomer page
    return render(request, 'payment_app/index.html', {'client_id': client_id} )

def customer_pagelink(request, client_id):    
    # Generate the URL using reverse
    url = reverse('customer_pagelink', kwargs={'client_id': client_id})
    # Render the template and pass it to the HttpResponse
    return render(request, 'customer_app/customer.html', {'client_id': client_id})
   

   

