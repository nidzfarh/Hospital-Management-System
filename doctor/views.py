from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from patient.models import Patient, Booking
from doctor.models import Doctor


# -----------------------------------
# DOCTOR DASHBOARD
# -----------------------------------

@login_required
def doctor_dashboard(request):

    total_patients = Patient.objects.count()

    try:

        # LOGGED-IN DOCTOR
        doctor = Doctor.objects.get(
            user=request.user
        )

        # ONLY THIS DOCTOR'S BOOKINGS
        recent_bookings = Booking.objects.filter(
            doctor=doctor
        ).order_by(
            'date',
            'time'
        )[:10]

        # TOTAL APPOINTMENTS
        today_appointments = Booking.objects.filter(
            doctor=doctor
        ).count()

        # UNIQUE PATIENTS
        today_patients = Booking.objects.filter(
            doctor=doctor
        ).values(
            'patient'
        ).distinct().count()

    except Doctor.DoesNotExist:

        recent_bookings = []

        today_appointments = 0

        today_patients = 0

    context = {

        'total_patients': total_patients,

        'today_patients': today_patients,

        'today_appointments': today_appointments,

        'recent_bookings': recent_bookings,

    }

    return render(

        request,

        'doctor/dashboard.html',

        context

    )


# -----------------------------------
# DOCTOR PROFILE
# -----------------------------------

@login_required
def doctor_profile(request):

    try:

        doctor = Doctor.objects.get(
            user=request.user
        )

    except Doctor.DoesNotExist:

        doctor = None

    context = {

        'doctor': doctor

    }

    return render(

        request,

        'doctor/profile.html',

        context

    )


# -----------------------------------
# DOCTOR APPOINTMENTS
# -----------------------------------

@login_required
def doctor_appointments(request):

    try:

        doctor = Doctor.objects.get(
            user=request.user
        )

        appointments = Booking.objects.filter(
            doctor=doctor
        ).order_by(
            '-date',
            '-time'
        )

    except Doctor.DoesNotExist:

        appointments = []

    context = {

        'appointments': appointments

    }

    return render(

        request,

        'doctor/appointments.html',

        context

    )