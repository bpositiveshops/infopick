from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('client_info', 'name', 'amount', 'status', 'created_date', 'last_updated')
    list_filter = ('client_info', 'name',  'amount', 'status',)
    search_fields = ('client_info__clientid', 'name', 'amount', 'status',)

