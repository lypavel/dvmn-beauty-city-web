from datetime import timedelta

from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

from .models import Employee, Salon, Service
from appointment.models import Appointment, Review
from accounts.models import Client


def get_reviews_spelling(total_reviews: int) -> str:
    word = 'отзыв'
    if total_reviews in (11, 12, 13, 14):
        spelling = word + 'ов'
    elif total_reviews % 10 == 1:
        spelling = word
    elif total_reviews % 10 in (2, 3, 4):
        spelling = word + 'а'
    else:
        spelling = word + 'ов'
    return spelling


def format_service_duration(duration: timedelta) -> str:
    total_minutes = duration.total_seconds() // 60

    if total_minutes in (11, 12, 13, 14):
        spelling = 'минут'
    elif total_minutes % 10 == 1:
        spelling = 'минута'
    elif total_minutes % 10 in (2, 3, 4):
        spelling = 'минуты'
    else:
        spelling = 'минут'
    return f'{round(total_minutes)} {spelling}'


def index(request):
    salons = [{
        'title': salon.title,
        'address': salon.address,
        'img': salon.img
    } for salon in Salon.objects.iterator()]

    services = [{
        'title': service.name,
        'price': f'{round(service.price)} ₽',
        'img': service.img
    } for service in Service.objects.iterator()]

    masters = [{
        'name': master.name,
        'img': master.photo,
        'review': f'{master.reviews.count()} '
        f'{get_reviews_spelling(master.reviews.count())}',
        'rating_img': master.rating_img,
        'spec': master.position,
        'experience': master.experience,
        'recording': ''
    } for master in Employee.objects.prefetch_related('reviews').iterator()]

    reviews = [{
        'name': review.name,
        'rating_img': review.rating_img,
        'text': review.text,
        'date': review.date
    } for review in Review.objects.iterator()]

    clients_count = Client.objects.count()

    context = {
        'salons': salons,
        'services': services,
        'masters': masters,
        'reviews': reviews,
        'clients_count': clients_count
    }
    return render(request, 'index.html', context=context)


# @login_required
@user_passes_test(lambda user: user.is_superuser)
def administrator(request):
    context = {
        'user':
            {
                'avatar': 'img/avatars/1.svg',
                'payment_per_month': '628 200',
                'visits_per_month': '349',
                'visits_per_year': '3 956',
                'percentage_of_visits': '100',
                'role': 'Администратор'
            }
    }

    # TODO добавить ссылки
    # TODO связать с базой данных
    return render(request, 'admin.html', context=context)


@login_required
def notes(request):
    appointments = Appointment.objects\
        .filter(client=request.user.id)\
        .select_related('service', 'employee', 'salon')
    print(appointments)
    paid_appointments = appointments.filter(is_paid=True)
    unpaid_appointments = appointments.filter(is_paid=False)
    print(paid_appointments)

    total_price = 0
    for appointment in unpaid_appointments:
        total_price += appointment.final_price

    context = {
        'unpaid_orders': unpaid_appointments,
        'paid_orders': paid_appointments,
        'total_price': total_price
    }
    # TODO добавить ссылки на оплату
    return render(request, 'notes.html', context=context)


def service_finally(request, appointment):
    context = {
        'order': {
            'time': '16:30',
            'date': '18 ноября',
            'id': '12345',
            'salon': 'BeautyCity Пушкинская',
            'address': 'ул. Пушкинская, д. 78А',
            'service': 'Дневной макияж',
            'price': '751',
            'master': 'Елена',
            'avatar': 'img/masters/avatar/vizajist1.svg',


        }
    }
    return render(request, 'service_finally.html', context=context)


def info(request):
    salons = Salon.objects.all()

    services = [{
            'title': service.name,
            'price': f'{round(service.price)} ₽',
            'img': service.img,
            'duration': format_service_duration(service.duration)
        } for service in Service.objects.iterator()]

    masters = [{
        'name': master.name,
        'img': master.photo,
        'review': f'{master.reviews.count()} '
        f'{get_reviews_spelling(master.reviews.count())}',
        'rating_img': master.rating_img,
        'position': master.position,
        'experience': master.experience,
        'schedule': [{
            'date': period.date,
            'salon': period.salon.title,
            'start_time': period.start_time,
            'end_time': period.end_time
        } for period in master.schedule.iterator()]
    } for master in Employee.objects
        .prefetch_related('reviews', 'schedule')
        .iterator()]

    # masters_schedule = masters.
    reviews = Review.objects.all()
    contacts = {'phone_number': '+7 (917) 902 38 00', 'email': 'hello@beauty.ru'}
    context = {
        'salons': salons,
        'services': services,
        'masters': masters,
        'reviews': reviews,
        'contacts': contacts,
    }

    return render(request, 'info.html', context=context)
