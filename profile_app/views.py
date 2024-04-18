from django.shortcuts import render, get_object_or_404, redirect
from infopick_app.models import Profile,Client
from django.http import HttpResponse
# from .forms import ProfileForm

# Create your views here.
def profile_details(request):
    # Logic to retrieve and pass profile data to the template
    profile_data = {}  # Replace this with your actual logic to fetch profile data
    return render(request, 'profile_app/profile.html', {'profile_data': profile_data})

# profile_manager/views.py
def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'profile_app/profile.html', {'profiles': profiles})

def profile_detail(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    return render(request, 'profile_app/profile.html', {'profile': profile})

def profile_create(request):
    if request.method == 'POST':
        # Process form submission
        client_name = request.POST.get('clientName')
        client, created = Client.objects.get_or_create(email=request.user, defaults={'clientname': client_name})
        print("clientname: ", client_name)
        return redirect('profile')  # Redirect to the profile page or any other appropriate URL after form submission
    else:
        # Render the form
        return render(request, 'profile_app/profile.html')

def profile_update(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        profile.save()
    return render(request, 'profile_app/profile.html')

def profile_delete(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        profile.delete()
        return redirect('profile_list')
    return render(request, 'profile_app/profile.html', {'profile': profile})
