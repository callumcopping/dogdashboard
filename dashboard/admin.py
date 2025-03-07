from django.contrib import admin
from .models import Client, Pet, Booking, UploadForm

admin.site.register(Client)
admin.site.register(Pet)
admin.site.register(Booking)
admin.site.register(UploadForm)
