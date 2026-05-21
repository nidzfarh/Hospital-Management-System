from django.urls import path
from . import views

urlpatterns = [

    path(
        'dashboard/',
        views.admin_dashboard,
        name='admin_dashboard'
    ),

    path(
        'doctors/',
        views.doctors_page,
        name='admin_doctors'
    ),

    path(
        'patients/',
        views.patients_page,
        name='admin_patients'
    ),

    path(
        'appointments/',
        views.appointments_page,
        name='admin_appointments'
    ),

]