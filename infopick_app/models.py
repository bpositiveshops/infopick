# models.py
import uuid
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Client(models.Model):
    clientname = models.CharField(max_length=100)
    clientid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.clientname
   




