from django.shortcuts import render

# Create your views here.

def customer_details(request):
    # Logic to retrieve and pass customer data to the template
    customer_data = {}  # Replace this with your actual logic to fetch customer data
    return render(request, 'customer_app/customer.html', {'customer_data': customer_data})
