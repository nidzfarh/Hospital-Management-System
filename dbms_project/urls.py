from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [

    path(
        'admin/',
        admin.site.urls
    ),

    path(
        'accounts/',
        include('accounts.urls')
    ),

    path(
        'patient/',
        include('patient.urls')
    ),

    path(
        'doctor/',
        include('doctor.urls')
    ),

    path(
        'adminpanel/',
        include('adminpanel.urls')
    ),

    path(
        '',
        RedirectView.as_view(
            pattern_name='login_page',
            permanent=False
        )
    ),

]