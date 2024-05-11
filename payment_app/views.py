from django.shortcuts import render
from .models import Order
from django.views.decorators.csrf import csrf_exempt
from .razorpay.client import Client
from .razorpay.utility import Utility
from .constants import PaymentStatus
from django.views.decorators.csrf import csrf_exempt
from infopick_app.models import ClientInfo
from django.conf import settings
import json

def index(request, client_id):
    return render(request, "payment_app/index.html", {'client_id': client_id})


def order_payment(request, client_id):
    if request.method == "POST":
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        client = Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))
        razorpay_order = client.order.create(
            {"amount": int(amount) * 100, "currency": "INR", "payment_capture": "1"}
        )
        # Assuming there is a foreign key relationship between Client and QRCode models
        clientinfo = ClientInfo.objects.filter(email=request.user, clientid=client_id).first()

        order = Order.objects.create(
            client_info = clientinfo, name=name, amount=amount, provider_order_id=razorpay_order["id"]
        )
        order.save()
        return render(
            request,
            "payment_app/payment.html",
            {
                "callback_url": "http://" + "localhost:8000" + "/razorpay/callback/",
                "razorpay_key": settings.RAZORPAY_API_KEY,
                "order": order,
            },
        )
    return render(request, "payment_app/payment.html")


@csrf_exempt
def callback(request):
    def verify_signature(response_data):
        # Instantiate the Client object
        client = Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))
        # Instantiate the Utility class with the client object
        utility = Utility(client)
        # Now you can use the utility object with the assigned client
        return utility.verify_payment_signature(response_data)

    if "razorpay_signature" in request.POST:
        payment_id = request.POST.get("razorpay_payment_id", "")
        provider_order_id = request.POST.get("razorpay_order_id", "")
        signature_id = request.POST.get("razorpay_signature", "")
        order = Order.objects.get(provider_order_id=provider_order_id)
        order.payment_id = payment_id
        order.signature_id = signature_id
        order.save()
        if verify_signature(request.POST):
            order.status = PaymentStatus.SUCCESS
            order.save()
            return render(request, "payment_app/callback.html", context={"status": order.status})
        else:
            order.status = PaymentStatus.FAILURE
            order.save()
            return render(request, "payment_app/callback.html", context={"status": order.status})
    else:
        payment_id = json.loads(request.POST.get("error[metadata]")).get("payment_id")
        provider_order_id = json.loads(request.POST.get("error[metadata]")).get(
            "order_id"
        )
        order = Order.objects.get(provider_order_id=provider_order_id)
        order.payment_id = payment_id
        order.status = PaymentStatus.FAILURE
        order.save()
        return render(request, "payment_app/callback.html", context={"status": order.status})