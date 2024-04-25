"""
URL configuration for infopick project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from infopick_app.views import *
from customer_app.views import *
from payment_app.views import *
from allauth.account.views import LoginView

urlpatterns = [
    path('', landing_page, name='landing-page'),
    path('profile/', profile, name='profile'),
    path('admin/', admin.site.urls),
    path('account/', include('allauth.urls')),
    path('account/<provider>/login/', LoginView.as_view(), name='socialaccount_login'),
    path('profile/', include('profile_app.urls')),  # Include profile app URLs
    path('customer/', include('customer_app.urls')),  # Include customer app URLs
    path('customer_list/', customer_list, name='customer_list'), #For debugging
    path("razorpay/", include('payment_app.urls'), name="urls"),  # Include Payment app URLs
    # path("razorpay/", include('payment_app.urls'), name="urls"),
    # Define a separate URL pattern for the debug_customer_list view
    # path('debug/customer_list/debug/', customer_list, name='customer_list'), //For debugging
]

