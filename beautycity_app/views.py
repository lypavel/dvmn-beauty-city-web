from django.shortcuts import render

from .models import Employee, Salon, Service
from appointment.models import Review


def index(request):
    salons = [{
        'title': salon.title,
        'address': salon.address,
        'img': salon.img
    } for salon in Salon.objects.iterator()]

    services = [{
        'title': service.name,
        'price': service.price,
        'img': service.img
    } for service in Service.objects.iterator()]

    masters = [{
        'name': master.name,
        'img': master.photo,
        'review': 'FIXME отзывов',
        'rating_img': master.rating_img,
        'spec': master.position,
        'experience': master.experience,
        'recording': ''
    } for master in Employee.objects.iterator()]

    reviews = [{
        'name': review.name,
        'rating_img': review.rating_img,
        'text': review.text,
        'date': review.date
    } for review in Review.objects.iterator()]

    context = {
        'salons': salons,
        'services': services,
        'masters': masters,
        'reviews': reviews,
    }

    # контекст из шаблона.
    # если количество контекста не соответствует весртка ломается
    # salons минимум 3 максимум 4
    # services минимум 4
    # reviews минимум 4
    # masters минимум 4
    # TODO добавить ссылки
    # TODO связать с базой данных
    # TODO заменить статичный контекст на контекст из базы данных
    # TODO при необходимости поправить стили чтобы количество данных не ломало страницу

    return render(request, 'index.html', context=context)


def administrator(request):
    # TODO добавить ссылки
    # TODO связать с базой данных
    # TODO почистить от статичных данных
    return render(request, 'admin.html')


def notes(request):
    # TODO добавить ссылки
    # TODO связать с базой данных
    # TODO почистить от статичных данных
    return render(request, 'notes.html')


def popup(request):
    # Сделано для пред просмотра
    # TODO добавить ссылки
    # TODO Разбить на отдельные popup

    return render(request, 'popup.html')


def service(request):
    # TODO добавить ссылки
    # TODO связать с базой данных
    # TODO почистить от статичных данных
    return render(request, 'service.html')


def service_finally(request):
    # TODO добавить ссылки
    # TODO связать с базой данных
    # TODO почистить от статичных данных
    return render(request, 'service_finally.html')