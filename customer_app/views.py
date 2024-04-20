from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse
# Create your views here.

def customer_create(request, client_id):
    # Assume you have the client_id available here
    client_id = '75bfcaf0-b77a-4508-b1b0-02d5ee389d80'

    # Generate the URL using reverse
    url = reverse('customer_create', kwargs={'client_id': client_id})

    # Render the template and pass it to the HttpResponse
    return render(request, 'customer_app/addcustomer.html', {'client_id': client_id})
   

