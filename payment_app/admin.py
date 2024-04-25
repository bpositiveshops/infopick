from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('clientid', 'name', 'amount', 'status', 'created_date', 'last_updated')
    list_filter = ('clientid', 'name',  'amount', 'status',)
    search_fields = ('clientid', 'name', 'amount', 'status',)

