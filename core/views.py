# core/views.py
from django.shortcuts import render

def landing_page(request):
    return render(request, 'core/home.html')
