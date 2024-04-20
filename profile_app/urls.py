from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('profile/create/', views.profile_create, name='profile_create'),
]