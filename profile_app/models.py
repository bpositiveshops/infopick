from django.db import models
from infopick_app.models import Client
from django.utils import timezone

class ClientQrcode(models.Model):
    clientid = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    dataqrcode =  models.BinaryField()
    created_date = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.clientid)
