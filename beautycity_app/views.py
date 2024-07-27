from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

from .models import Employee, Salon, Service
from appointment.models import Appointment, Review


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

    clients_count = 1000
    # FIXME: загружать количество зарегистрированных пользователей из бд

    context = {
        'salons': salons,
        'services': services,
        'masters': masters,
        'reviews': reviews,
        'clients_count': clients_count
    }

    # контекст из шаблона.
    # если количество контекста не соответствует весртка ломается
    # salons минимум 3 максимум 4
    # services минимум 4
    # reviews минимум 4
    # masters минимум 4
    # TODO связать с базой данных
    # TODO заменить статичный контекст на контекст из базы данных
    # TODO при необходимости поправить стили чтобы количество данных не ломало страницу

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
    # TODO связать с базой данных
    # TODO почистить от статичных данных
    return render(request, 'notes.html', context=context)


def popup(request):
    # Сделано для пред просмотра
    # TODO добавить ссылки
    # TODO Разбить на отдельные popup

    return render(request, 'popup.html')


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
    # TODO добавить ссылки
    # TODO связать с базой данных
    return render(request, 'service_finally.html', context=context)


def info(request):
    salons = Salon.objects.all()
    services = Service.objects.all()
    masters = Employee.objects.all()
    reviews = Review.objects.all()
    contacts = ['Тел. +7 777 777 77 77', 'Почта 6ydb_KpacuBou@po4ta.ru']
    context = {
        'salons': salons,
        'services': services,
        'masters': masters,
        'reviews': reviews,
        'contacts': contacts,
    }

    return render(request, 'info.html', context=context)

