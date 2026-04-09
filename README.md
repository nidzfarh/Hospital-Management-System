# DBMS Project

A Django-based database management system project with authentication and doctor management features.

## Overview

This project includes:
- `accounts` app: user registration and login
- `doctor` app: doctor dashboard, profile view, and logout
- `patient` app: patient-related models and functionality

The project is configured for PostgreSQL in `dbms_project/settings.py`.

## Features

- User login and registration pages
- Doctor dashboard and profile pages
- Authentication-enforced profile access
- Admin interface available at `/admin/`

## Requirements

- Python 3.11+ (or compatible)
- Django 5.2.5
- PostgreSQL
- A virtual environment is recommended

## Configuration

1. Activate your virtual environment:

```powershell
& .\venv\Scripts\Activate.ps1
```

2. Install dependencies (if requirements are available):

```powershell
pip install django
```

3. Configure PostgreSQL credentials in `dbms_project/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dbms_project',
        'USER': 'postgres',
        'PASSWORD': 'dbmspsql',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

4. Create the database and run migrations:

```powershell
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser:

```powershell
python manage.py createsuperuser
```

## Running the Project

Start the development server:

```powershell
python manage.py runserver
```

Then open:
- `http://127.0.0.1:8000/login/` for login
- `http://127.0.0.1:8000/register/` for registration
- `http://127.0.0.1:8000/doctor/dashboard/` for doctor dashboard
- `http://127.0.0.1:8000/doctor/profile/` for doctor profile

## URL Routing

- `/register/` → `accounts.views.register`
- `/login/` → `accounts.views.user_login`
- `/doctor/dashboard/` → `doctor.views.doctor_dashboard`
- `/doctor/profile/` → `doctor.views.doctor_profile`
- `/doctor/logout/` → `doctor.views.doctor_logout`

## Notes

- `DEBUG` is currently enabled in development settings.
- `SECRET_KEY` should be replaced before deploying to production.
- Static files are served from the `static/` directory.
- Templates include `login.html`, `registration.html`, and doctor templates under `doctor/templates/doctor/`.
