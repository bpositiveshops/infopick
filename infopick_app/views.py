# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *

@login_required
def profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
        # client, created = Client.objects.get_or_create(email=request.user, defaults={'clientname': 'Grand PG'})
        # print("client: ", client.email)
    except Profile.DoesNotExist:
        # Redirect to a page where the user can complete their profile
        messages.warning(request, 'Please complete your profile.')
        return redirect('socialaccount_signup')  # Change to the appropriate URL name for the signup page
    return render(request, 'infopick_app/main.html', {'profile': profile})
    # return render(request, 'account/profile.html', {'profile': profile, 'client': client})

def landing_page(request):
    return render(request, 'infopick_app/home.html')


