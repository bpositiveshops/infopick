from django.contrib import admin
from .models import *

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('custname', 'email', 'phone', 'client_info', 'created_date', 'last_updated')
    list_filter = ('client_info', 'created_date', 'last_updated')
    search_fields = ('client_info__clientid','custname', 'email', 'phone')
