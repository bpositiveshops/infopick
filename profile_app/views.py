import qrcode
from django.shortcuts import render, get_object_or_404, redirect
from infopick_app.models import Profile,ClientInfo
from profile_app.models import ClientQrcode
from django.http import JsonResponse
from io import BytesIO
import base64
import json
from django.db import transaction
from django.utils import timezone

def profile_create(request):
    if request.method == 'POST':
        # Process form submission
        client_name = request.POST.get('clientName')
        location = request.POST.get('location')
        phone = request.POST.get('phone')
        # Create Client Object
        client, created = ClientInfo.objects.get_or_create(email=request.user, clientname=client_name, location=location, phone=phone)
        
        # Assuming generate_qr_code function has been called and it returns a JsonResponse
        json_response = generate_qr_code(client)
        
        # Check the content of the JSON response
        if json_response.status_code == 200:
            json_data = json.loads(json_response.content)
            print("json_data:", json_data)          
        else:
            print("Error:", json_response.content)
     
        return JsonResponse({'message': 'Profile created successfully'})  # Return a JsonResponse
    else:
        # Render the form
        return render(request, 'profile_app/profile_list.html')
    
@transaction.atomic
def generate_qr_code(client):
    try:
        # Generate QRCode
        qr_code = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr_code.add_data(f"http://localhost:8000/customer/{str(client.clientid)}")
        qr_code.make(fit=True)
        img = qr_code.make_image(fill_color="black", back_color="white")

        # Convert image data to byte string
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        image_data = buffer.getvalue()

        # Try to retrieve the ClientQrcode object based on clientid
        client_qrcode = ClientQrcode.objects.get(clientid=client)
        # Store the QRCode for user
        # client_qrcode, created = ClientQrcode.objects.get_or_create(clientid=client, dataqrcode=image_data_base64)
        return JsonResponse({'message': 'QRcode already exists'})
    
    except ClientQrcode.DoesNotExist:
         # Create a new ClientQrcode object if it doesn't exist
        client_qrcode = ClientQrcode(clientid=client)
        client_qrcode.dataqrcode = image_data
        client_qrcode.save()
        return JsonResponse({'error': 'QRcode generated successfully'})
    
    except Exception as e:
        return JsonResponse({'error': str(e)})

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
