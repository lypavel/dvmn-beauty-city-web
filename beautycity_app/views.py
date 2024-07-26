from django.shortcuts import render


def index(request):
    context = {
        'salons': [
            {
                'title': 'BeautyCity Пушкинская',
                'address': 'ул. Пушкинская, д. 78А',
                'img': 'img/salons/salon1.svg',
            },
            {
                'title': 'BeautyCity Ленина',
                'address': 'ул. Ленина, д. 211',
                'img': 'img/salons/salon2.svg',
            },
            {
                'title': 'BeautyCity Красная',
                'address': 'ул. Красная, д. 10',
                'img': 'img/salons/salon3.svg',
            },
        ],
        'services': [
            {
                'title': 'Дневной макияж',
                'price': '1 400 ₽',
                'img': 'img/services/service1.svg',
            },
            {
                'title': 'Маникюр. Классический. Гель',
                'price': '2 000 ₽',
                'img': 'img/services/service2.svg',
            },
            {
                'title': 'Укладка волос',
                'price': '1 500 ₽',
                'img': 'img/services/service3.svg',
            },
            {
                'title': 'Укладка волос',
                'price': '3 000 ₽',
                'img': 'img/services/service4.svg',
            },
            {
                'title': 'Педикюр',
                'price': '1 000 ₽',
                'img': 'img/services/service5.svg',
            },
            {
                'title': 'Окрашивание волос',
                'price': '5 000 ₽',
                'img': 'img/services/service6.svg',
            },
        ],
        'masters': [
            {
                'name': 'Елизавета Лапина',
                'img': 'img/masters/master1.svg',
                'review': '24 отзыва',
                'rating_img': 'img/rating.svg',
                'spec': 'Мастер маникюра',
                'experience': '3 г. 10 мес.',
                'recording': '',
            },
            {
                'name': 'Анастасия Сергеева',
                'img': 'img/masters/master2.svg',
                'review': '',
                'rating_img': 'img/rating.svg',
                'spec': 'Парикмахер',
                'experience': '4 г. 9 мес.',
                'recording': '',
            },
            {
                'name': 'Ева Колесова',
                'img': 'img/masters/master3.svg',
                'review': '18 отзывов',
                'rating_img': 'img/rating.svg',
                'spec': 'Визажист',
                'experience': '1 г. 2 мес.',
                'recording': '',
            },
            {
                'name': 'Мария Суворова',
                'img': 'img/masters/master4.svg',
                'review': '32 отзыва',
                'rating_img': 'img/rating.svg',
                'spec': 'Стилист',
                'experience': '1 г. 1 мес.',
                'recording': '',
            },
            {
                'name': 'Мария Максимова',
                'img': 'img/masters/master5.svg',
                'review': '42 отзыва',
                'rating_img': 'img/rating.svg',
                'spec': 'Стилист',
                'experience': '3 г. 1 мес.',
                'recording': '',

            },
            {
                'name': 'Майя Соболева',
                'img': 'img/masters/master6.svg',
                'review': '32 отзыва',
                'rating_img': 'img/rating.svg',
                'spec': 'Визажист',
                'experience': '1 г. 1 мес.',
                'recording': '',
            },
        ],
        'reviews': [
            {
                'name': 'Светлана Г.',
                'rating_img': 'img/rating.svg',
                'text': '''Отличное место для красоты, очень доброжелательный и отзывчивый персонал, девочки заботливые,
                аккуратные и большие профессионалы. Посещаю салон с самого начала,
                но он не теряет своей привлекательности, как в обслуживании.''',
                'date': '12 ноября 2022',
            },
            {
                'name': 'Ольга Н.',
                'rating_img': 'img/rating.svg',
                'text': '''Мне всё лень было отзыв писать, но вот "руки дошли". Несколько раз здесь
                стриглась, мастера звали, кажется, Катя. Все было отлично, приятная молодая женщина
                и по стрижке вопросов не было)''',
                'date': '5 ноября 2022',
            },
            {
                'name': 'Елена В.',
                'rating_img': 'img/rating.svg',
                'text': '''Делала процедуру микротоки у мастера Светланы .
                 Светлана внимательная, приветливая, ненавязчивая.
                  Рекомендую и мастера, и процедуру. Еще делала бровки у Татьяны ,
                   я в восторге , брови просто идеально сдеданы''',
                'date': '28 октября 2022',
            },
            {
                'name': 'Виктория Г.',
                'rating_img': 'img/rating.svg',
                'text': '''Была на педикюре у Ольги. Очень понравилось. Все инструменты стерильные,
                 упакованы в крафт-пакет. Для меня очень важно было. Оборудование новое. ''',
                'date': '13 октября 2022',
            },
            {
                'name': 'Анастасия Е.',
                'rating_img': 'img/rating.svg',
                'text': '''Сегодня прокололи ушки дочке в этом салоне) Остались довольны обслуживанием и персоналом.
                 Девочки очень приветливые и внимательные . Спасибо большое, всё понравилось)''',
                'date': '8 октября 2022',
            },
            {
                'name': 'Алина Ц.',
                'rating_img': 'img/rating.svg',
                'text': '''Отличный салон, сервис на самом высоком уровне,
                 всем мастерам огромное уважение за труд, обязательно вернусь''',
                'date': '1 октября 2022',
            },
        ],
        'clients_count': '1001',
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


def administrator(request):
    context = {
        'admin':
            {
                'avatar': 'img/avatars/1.svg',
                'payment_per_month': '628 200',
                'visits_per_month': '349',
                'visits_per_year': '3 956',
                'percentage_of_visits': '100',
            }
    }

    # TODO добавить ссылки
    # TODO связать с базой данных
    return render(request, 'admin.html', context=context)


def notes(request):
    context = {
        'user': {
            'avatar': '',
            'name': '',
        },
        'unpaid_orders': [
            {
                'service': 'Дневной макияж',
                'service_img': 'img/icons/list.svg',
                'master': 'Ева Колесова',
                'price': '1 400',
                'id': '23184',
                'date': '29 ноября',
                'time': '13:30',
            }
        ],
        'paid_orders': [
            {
                'service': '',
                'service_img': '',
                'master': '',
                'price': '',
                'id': '',
                'date': '',
                'time': '',
            }
        ],
        'total_price': '3 900 руб'
    }
    # TODO добавить ссылки
    # TODO связать с базой данных
    # TODO почистить от статичных данных
    return render(request, 'notes.html', context=context)


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