from django.db import models
from infopick_app.models import Client
from django.utils import timezone

class Customer(models.Model):
    custname = models.CharField(max_length=100)  # Add custname field
    email = models.EmailField()  # Add email field
    phone = models.CharField(max_length=20)  # Add phone field
    clientid = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.custname
