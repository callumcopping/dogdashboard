"""
URL configuration for dogboarding project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from dashboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_redirect, name='home_redirect'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/clients/', views.client_list, name='client_list'),
    path('dashboard/pets/', views.pet_list, name='pet_list'),
    path('dashboard/bookings/', views.booking_list, name='booking_list'),
    path('dashboard/upload_forms/', views.upload_form_list, name='upload_form_list'),
    path('dashboard/add_client/', views.add_client, name='add_client'),
    path('dashboard/add_pet/', views.add_pet, name='add_pet'),
    path('dashboard/add_booking/', views.add_booking, name='add_booking'),
    path('dashboard/add_upload_form/', views.add_upload_form, name='add_upload_form'),
    path('dashboard/client/<int:client_id>/', views.client_detail, name='client_detail'),
    path('dashboard/pet/<int:pet_id>/', views.pet_detail, name='pet_detail'),
    path('dashboard/booking/<int:booking_id>/', views.booking_detail, name='booking_detail'),
    path('dashboard/upload_form/<int:upload_form_id>/', views.upload_form_detail, name='upload_form_detail'),
    path('dashboard/delete_client/<int:client_id>/', views.delete_client, name='delete_client'),
    path('dashboard/delete_pet/<int:pet_id>/', views.delete_pet, name='delete_pet'),
    path('dashboard/delete_booking/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    path('dashboard/delete_upload_form/<int:upload_form_id>/', views.delete_upload_form, name='delete_upload_form'),
    path('dashboard/calendar/', views.calendar_view, name='calendar_view'),
    path('dashboard/booking_events/', views.booking_events, name='booking_events'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
