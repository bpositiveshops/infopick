from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('create/', views.profile_create, name='profile_create'),
]