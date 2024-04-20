import qrcode
from django.shortcuts import render, get_object_or_404, redirect
from infopick_app.models import Profile,Client
from profile_app.models import ClientQrcode
from django.http import JsonResponse
from io import BytesIO

def profile_create(request):
    if request.method == 'POST':
        # Process form submission
        client_name = request.POST.get('clientName')

        print("clientname: ", client_name)
        # Create Client Object
        client, created = Client.objects.get_or_create(email=request.user, clientname=client_name)
        
        # Assuming there is a foreign key relationship between Client and QRCode models
        client = Client.objects.filter(email=request.user).first()

        # Generate QRCode
        qr_code = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=4,)
        qr_code.add_data(f"http://localhost:8000/customer/{client.clientid}")  # Change URL as needed
        qr_code.make(fit=True)
        img = qr_code.make_image(fill_color="black", back_color="white")
 
        # Convert image data to byte string
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        image_data = buffer.getvalue()

        # Store the QRCode for user
        clientqrcode, created = ClientQrcode.objects.get_or_create(clientid=client, dataqrcode=image_data)
        # return redirect('profile')  # Redirect to the profile page or any other appropriate URL after form submission
        return JsonResponse({'message': 'Profile created successfully'})  # Return a JsonResponse
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
