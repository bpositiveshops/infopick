# views.py
import base64
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from profile_app.models import *
from customer_app.models import *
from payment_app.models import *

@login_required
def profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
        # Retrieve the Clients for given user
        client = ClientInfo.objects.filter(email=request.user).first()
        # Define client_qrcode variable
        client_qrcode = None
        # Retrieve QR code data for the current user
        if client:
            client_qrcode = ClientQrcode.objects.filter(clientid=client).first()
        # Check if client_qrcode is not None and convert dataqrcode to base64
        if client_qrcode:
            client_qrcode.dataqrcode = base64.b64encode(client_qrcode.dataqrcode).decode('utf-8')
        # Retrieve the list of customers from the database
        customer_list = Customer.objects.all()
        # Retrieve the list of Orders from the database
        order_list = Order.objects.all()

    except Profile.DoesNotExist:
        # Redirect to a page where the user can complete their profile
        messages.warning(request, 'Please complete your profile.')
        return redirect('socialaccount_signup')  # Change to the appropriate URL name for the signup page
    return render(request, 'infopick_app/main.html', {'profile': profile, 'client_qrcode': client_qrcode, 'customer_list': customer_list, 'order_list': order_list}) 

def landing_page(request):
    return render(request, 'infopick_app/home.html')


