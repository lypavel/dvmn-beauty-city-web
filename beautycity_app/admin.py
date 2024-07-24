from django.contrib import admin
from .models import Salon, Service, Employee, EmployeeSchedule, Category


@admin.register(Salon)
class SalonAdmin(admin.ModelAdmin):
    list_display = ['title', 'address']
    search_fields = ['title', 'address']
    filter_horizontal = ['masters']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'duration']
    search_fields = ['name']
    list_filter = ['category']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'rating', 'experience']
    search_fields = ['name', 'position']
    filter_horizontal = ['services']


@admin.register(EmployeeSchedule)
class EmployeeScheduleAdmin(admin.ModelAdmin):
    list_display = ['employee', 'salon', 'date', 'start_time', 'end_time']
    search_fields = ['employee__name', 'salon__title']
    list_filter = ['date']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


admin.site.site_header = 'Панель управления салоном красоты'
