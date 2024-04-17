# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *

@login_required
def profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
        print("profile: ", request.user)
    except Profile.DoesNotExist:
        # Redirect to a page where the user can complete their profile
        messages.warning(request, 'Please complete your profile.')
        return redirect('socialaccunt/signup.html')  # Change 'socialaccunt/signup.html' to the appropriate URL name
    return render(request, 'account/profile.html', {'profile': profile})

