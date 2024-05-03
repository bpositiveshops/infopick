# admin.py
from django.contrib import admin
from .models import *

@admin.register(ClientInfo)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('clientname', 'location', 'phone', 'clientid', 'email', 'created_date', 'last_updated')
    list_filter = ('clientname', 'location', 'phone', 'clientid',  'email')
    search_fields = ['clientname', 'location', 'phone', 'clientid', 'email__email','created_date', 'last_updated']
