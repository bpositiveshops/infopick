from django.contrib import admin
from .models import *

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('custname', 'email', 'phone', 'clientid', 'created_date', 'last_updated')
    list_filter = ('clientid', 'created_date', 'last_updated')
    search_fields = ('clientid__clientid','custname', 'email', 'phone')
