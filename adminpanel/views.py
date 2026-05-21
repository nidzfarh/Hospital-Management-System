from django.shortcuts import render

from patient.models import Patient, Booking
from doctor.models import Doctor
from accounts.models import CustomUser


# -----------------------------
# ADMIN DASHBOARD
# -----------------------------

def admin_dashboard(request):

    context = {

        'patients_count':
        Patient.objects.count(),

        'doctors_count':
        Doctor.objects.count(),

        'bookings_count':
        Booking.objects.count(),

        'users_count':
        CustomUser.objects.count(),

        'recent_bookings':
        Booking.objects.all().order_by('-created_at')[:10]

    }

    return render(
        request,
        'adminpanel/dashboard.html',
        context
    )


# -----------------------------
# DOCTORS PAGE
# -----------------------------

def doctors_page(request):

    doctors = Doctor.objects.all()

    context = {

        'doctors': doctors

    }

    return render(
        request,
        'adminpanel/doctors.html',
        context
    )


# -----------------------------
# PATIENTS PAGE
# -----------------------------

def patients_page(request):

    patients = Patient.objects.all()

    context = {

        'patients': patients

    }

    return render(
        request,
        'adminpanel/patients.html',
        context
    )


# -----------------------------
# APPOINTMENTS PAGE
# -----------------------------

def appointments_page(request):

    bookings = Booking.objects.all().order_by('-date')

    context = {

        'bookings': bookings

    }

    return render(
        request,
        'adminpanel/appointments.html',
        context
    )