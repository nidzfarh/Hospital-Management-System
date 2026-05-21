from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse

from .models import CustomUser
from patient.models import Patient
from doctor.models import Doctor


# -----------------------------------
# TEST VIEW
# -----------------------------------

def test(request):

    print("hello")

    return redirect('login_page')


# -----------------------------------
# GET DOCTORS AJAX
# -----------------------------------

def get_doctors(request):

    selected_spec = request.GET.get(
        'specialization'
    )

    doctors = []

    if selected_spec:

        doctors_qs = Doctor.objects.filter(
            specialization__iexact=selected_spec
        )

        doctors = list(

            doctors_qs.values(
                "id",
                "fullname"
            )

        )

    return JsonResponse({
        'doctors': doctors
    })


# -----------------------------------
# LOGIN PAGE
# -----------------------------------

def login_page(request):

    if request.method == "POST":

        username = request.POST.get(
            "username"
        )

        password = request.POST.get(
            "password"
        )

        user = authenticate(

            request,

            username=username,

            password=password

        )

        if user is not None:

            login(request, user)

            # ADMIN
            if user.role == 'admin':

                return redirect(
                    'admin_dashboard'
                )

            # DOCTOR
            elif user.role == 'doctor':

                return redirect(
                    'doctor_dashboard'
                )

            # PATIENT
            elif user.role == 'patient':

                return redirect(
                    'dashboard'
                )

            else:

                return redirect(
                    'login_page'
                )

        else:

            messages.error(
                request,
                "Invalid username or password"
            )

    return render(
        request,
        "login.html"
    )


# -----------------------------------
# REGISTRATION PAGE
# -----------------------------------

def registration_page(request):

    return render(
        request,
        'registration.html'
    )


# -----------------------------------
# REGISTER USER
# -----------------------------------

def register(request):

    if request.method == 'POST':

        role = request.POST.get('role')

        username = request.POST.get(
            'username'
        )

        email = request.POST.get(
            'email'
        )

        password = request.POST.get(
            'password'
        )

        # CHECK EXISTING USER
        if CustomUser.objects.filter(
            username=username
        ).exists():

            messages.error(
                request,
                "Username already exists!"
            )

            return redirect(
                'registration_page'
            )

        # CREATE USER
        user = CustomUser.objects.create_user(

            username=username,

            email=email,

            password=password,

            role=role

        )

        # -----------------------------------
        # PATIENT REGISTRATION
        # -----------------------------------

        if role == 'patient':

            patient_name = request.POST.get(
                'patient_name'
            )

            patient_age = request.POST.get(
                'patient_age'
            )

            patient_gender = request.POST.get(
                'patient_gender'
            )

            phone_number = request.POST.get(
                'phone_number'
            )

            Patient.objects.create(

                user=user,

                first_name=patient_name,

                last_name='',

                age=patient_age,

                gender=patient_gender,

                email=email,

                phone_number=phone_number

            )

        # -----------------------------------
        # DOCTOR REGISTRATION
        # -----------------------------------

        elif role == 'doctor':

            fullname = request.POST.get(
                'doctor_name'
            )

            specialization = request.POST.get(
                'specialization'
            )

            experience = request.POST.get(
                'experience'
            )

            Doctor.objects.create(

                user=user,

                fullname=fullname,

                specialization=specialization,

                experience=experience

            )

        messages.success(

            request,

            "Registration successful! Please login."

        )

        return redirect(
            'login_page'
        )

    return render(
        request,
        'registration.html'
    )


# -----------------------------------
# LOGOUT
# -----------------------------------

def logout_view(request):

    logout(request)

    return redirect(
        'login_page'
    )