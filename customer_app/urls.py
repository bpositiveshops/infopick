from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('<uuid:client_id>/', views.customer_create, name='customer_create'),
]