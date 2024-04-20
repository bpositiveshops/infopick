
from django.contrib import admin
from .models import *


@admin.register(ClientQrcode)
class QrcodeAdmin(admin.ModelAdmin):
    list_display = ('clientid', 'dataqrcode', 'created_date', 'last_updated')
    list_filter = ('clientid', 'dataqrcode')
    search_fields = ['clientid__clientid', 'dataqrcode', 'created_date', 'last_updated']