from datetime import timedelta, datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

from accounts.models import Client
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


def approve_appointment(request):
    if request.method == 'GET':
        request.session['salon_id'] = request.GET.get('selectSalon')
        request.session['date'] = request.GET.get('inputDate')
        request.session['service_id'] = request.GET.get('selectService')
        request.session['master_id'] = request.GET.get('selectMaster')
        request.session['time'] = request.GET.get('availableSlots')
        date = slot = ''

        try:
            salon = Salon.objects.get(id=request.session['salon_id'])
            service = Service.objects.get(id=request.session['service_id'])
            master = Employee.objects.get(id=request.session['master_id'])
            date = request.session['date']
            slot = request.session['time']
        except Salon.DoesNotExist:
            return HttpResponse('Не выбран салон')
        except Service.DoesNotExist:
            return HttpResponse('Не выбрана услугу')
        except Employee.DoesNotExist:
            return HttpResponse('Не выбран мастер')
        except date == '':
            return HttpResponse('Не выбрана дата')
        except slot == '':
            return HttpResponse('Не выбрано время')

        context = {
            'salon': salon,
            'date': date,
            'service': service,
            'master': master,
            'time': slot
        }
        return render(request, 'service_finally.html', context=context)

    if request.method == 'POST':
        fname = request.POST.get('fname')
        phone = request.POST.get('tel')
        comment = request.POST.get('contactsTextarea')
        client, created = Client.objects.get_or_create(
            phone_number=phone,
            defaults={
                'username': fname,
                'comment': comment
            }
        )

        start_time = datetime.strptime(request.session['time'], '%H:%M').time()
        service = Service.objects.get(id=request.session['service_id'])
        appointment = Appointment.objects.create(
            salon=Salon.objects.get(id=request.session['salon_id']),
            client=client,
            service=service,
            employee=Employee.objects.get(id=request.session['master_id']),
            final_price=service.price,
            date=datetime.strptime(request.session['date'], '%Y-%m-%d').date(),
            start_time=start_time,
            end_time=(datetime.combine(datetime.today(), start_time) + service.duration).time()
        )
        return redirect('index')



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
    service_length = Service.objects.get(id=service_id).duration
    if schedule:
        # Список существующих записей для текущего мастера и даты
        existing_appointments = list(Appointment.objects.filter(
            date=date,
            employee_id=master_id
        ).values('start_time', 'end_time'))

        start_time = schedule.start_time
        end_time = schedule.end_time

        while end_time > start_time:
            # Проверка, не пересекаются ли время начала и конец нового слота с существующими записями
            overlaps = any(
                (start_time < datetime.combine(datetime.today(), appt['end_time']).time() and
                 (datetime.combine(datetime.today(), start_time) + service_length).time() > appt['start_time'])
                for appt in existing_appointments
            )
            if not overlaps:
                time_slots.append(start_time)

            dt = datetime.combine(datetime.today(), start_time) + timedelta(minutes=30)
            start_time = dt.time()
            if (datetime.combine(datetime.today(), start_time) + service_length).time() > end_time:
                break
    formatted_slots = [slot.strftime('%H:%M') for slot in time_slots]
    slots_html = render(request, "partials/get_slots.html", {'slots': formatted_slots})

    return HttpResponse(slots_html)
