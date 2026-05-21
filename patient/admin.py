from django.contrib import admin
from .models import Patient, Booking

admin.site.register(Patient)
admin.site.register(Booking)