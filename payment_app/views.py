from django.shortcuts import render

# Create your views here.

def payment_details(request):
    # Logic to retrieve and pass payment data to the template
    payment_data = {}  # Replace this with your actual logic to fetch payment data
    return render(request, 'payment_app/payment.html', {'payment_data': payment_data})
