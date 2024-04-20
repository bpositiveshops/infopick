# admin.py
from django.contrib import admin
from .models import *

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('clientname', 'clientid', 'email', 'created_date', 'last_updated')
    list_filter = ('clientname', 'clientid', 'email')
    search_fields = ['clientname', 'clientid', 'email__email','created_date', 'last_updated']
