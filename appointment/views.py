from datetime import timedelta, datetime

from django.http import HttpResponse
from django.shortcuts import render

from appointment.models import Appointment
from beautycity_app.models import Salon, Service, Category, Employee, EmployeeSchedule


def get_service(request):
    salons = Salon.objects.all()
    categories = Category.objects.all()
    context = {
        'salons': salons,
        'categories': categories

    }
    return render(request, 'service.html', context)


def get_masters(request):
    salon_id = request.GET.get('selectSalon')
    service_id = request.GET.get('selectService')
    masters = Employee.objects.filter(salons__id__in=salon_id, services__id=service_id)
    return render(request, 'partials/get_masters.html', {'masters': masters})


def get_services(request):
    category_id = request.GET.get('selectCategory')
    services = Service.objects.filter(category_id=category_id)
    return render(request, 'partials/get_services.html', {'services': services})


def get_slots(request):
    salon_id = request.GET.get('selectSalon')
    category_id = request.GET.get('selectCategory')
    date = request.GET.get('inputDate')
    service_id = request.GET.get('selectService')
    master_id = request.GET.get('selectMaster')
    try:
        schedule = EmployeeSchedule.objects.get(salon_id=salon_id, date=date, employee_id=master_id)
    except EmployeeSchedule.DoesNotExist:
        schedule = None
    time_slots = []
    while schedule and schedule.end_time > schedule.start_time:
        time_slots.append(schedule.start_time)
        dt = datetime.combine(datetime.today(), schedule.start_time)
        new_dt = dt + timedelta(minutes=30)
        schedule.start_time = new_dt.time()
    available_slots = []
    for slot in time_slots:
        if not Appointment.objects.filter(date=date, start_time__lte=slot, end_time__gt=slot).exists():
            available_slots.append(slot)
    formatted_slots = [slot.strftime('%H:%M') for slot in available_slots]
    slots_html = render(request, "partials/get_slots.html", {'slots': formatted_slots})

    return HttpResponse(slots_html)
