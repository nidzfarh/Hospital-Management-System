from django.urls import path

from . import views

urlpatterns = [

    path(
        '',
        views.test,
        name='test'
    ),

    path(
        'login/',
        views.login_page,
        name='login_page'
    ),

    path(
        'register/',
        views.registration_page,
        name='registration_page'
    ),

    path(
        'register-user/',
        views.register,
        name='register'
    ),

    path(
        'get-doctors/',
        views.get_doctors,
        name='get_doctors'
    ),

    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),

]