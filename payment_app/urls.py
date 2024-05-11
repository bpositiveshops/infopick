from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("payment/<uuid:client_id>/", views.order_payment, name="payment"),
    path("callback/", views.callback, name="callback"),
]
