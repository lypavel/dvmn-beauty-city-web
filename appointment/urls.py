from django.urls import path

from appointment.views import get_service, get_services, get_masters, get_slots, approve_appointment

app_name = 'appointment'

urlpatterns = [
    path('service', get_service, name='service'),
    path('get_services', get_services, name='get_services'),
    # path('get_categories', get_categories, name='get_categories'),
    path('get_masters', get_masters, name='get_masters'),
    path('get_slots', get_slots, name='get_slots'),
    path('approve_appointment', approve_appointment, name='approve_appointment'),
]
