from django.urls import path
from . import views

urlpatterns = [
    path('create-appointment/', views.create_appointment, name='create_appointment'),
    path('manage-appointments/', views.manage_appointments, name='manage_appointments'),
    path('appointment-list/', views.appointment_list, name='appointment_list'),
    path('home/', views.home, name='home'),
]
