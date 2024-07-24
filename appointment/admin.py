from django.contrib import admin

from appointment.models import Appointment, Review


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['client', 'employee', 'service', 'final_price', 'date', 'start_time', 'end_time']
    search_fields = ['client__username', 'employee__name', 'service__name']
    list_filter = ['date', 'employee']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'text', 'date']
    search_fields = ['date', 'name', 'rating']
    list_filter = ['date', 'rating']


