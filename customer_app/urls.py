from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('<uuid:client_id>/', views.customer_pagelink, name='customer_pagelink'),
    path('add-customer/<uuid:client_id>/', views.add_customer, name='add_customer'),
    path('customer_pay/<uuid:client_id>/', views.customer_pay, name='customer_pay'),
    path('customer_list/', views.customer_list, name='customer_list'),
]