import os
import django
import random
from faker import Faker

# -----------------------------------
# DJANGO SETUP
# -----------------------------------

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "dbms_project.settings"
)

django.setup()

# -----------------------------------
# IMPORT MODELS
# -----------------------------------

from accounts.models import CustomUser
from patient.models import Patient, Booking
from doctor.models import Doctor

fake = Faker()

# -----------------------------------
# CREATE DOCTORS
# -----------------------------------

specializations = [
    "Cardiologist",
    "Dermatologist",
    "Neurologist",
    "Orthopedic",
    "Pediatrician",
    "ENT Specialist",
    "Psychiatrist",
    "General Physician"
]

doctors = []

for i in range(10):

    user = CustomUser.objects.create_user(

        username=f"doctor{i}",

        email=fake.email(),

        password="test123",

        role="doctor"

    )

    doctor = Doctor.objects.create(

        fullname=f"Dr. {fake.name()}",

        specialization=random.choice(
            specializations
        ),

        experience=random.randint(2,25)

    )

    doctors.append(doctor)

print("Doctors created")


# -----------------------------------
# CREATE PATIENTS
# -----------------------------------

patients = []

for i in range(50):

    user = CustomUser.objects.create_user(

        username=f"patient{i}",

        email=fake.email(),

        password="test123",

        role="patient"

    )

    patient = Patient.objects.create(

        user=user,

        first_name=fake.first_name(),

        last_name=fake.last_name(),

        age=random.randint(18,80),

        gender=random.choice(["M","F","O"]),

        email=fake.email(),

        phone_number=fake.phone_number(),

        address=fake.address(),

        medical_history=fake.text(
            max_nb_chars=120
        )

    )

    patients.append(user)

print("Patients created")


# -----------------------------------
# CREATE BOOKINGS
# -----------------------------------

reasons = [

    "Routine Checkup",

    "Fever",

    "Skin Allergy",

    "Back Pain",

    "Headache",

    "Chest Pain",

    "Cold and Cough"

]

for i in range(100):

    user = random.choice(patients)

    patient_obj = Patient.objects.get(
        user=user
    )

    Booking.objects.create(

        patient=user,

        patient_full_name=
        f"{patient_obj.first_name} "
        f"{patient_obj.last_name}",

        doctor=random.choice(doctors),

        date=fake.date_between(

            start_date='-30d',

            end_date='+30d'

        ),

        time=fake.time(),

        reason=random.choice(reasons)

    )

print("Bookings created")

print("Database successfully populated!")