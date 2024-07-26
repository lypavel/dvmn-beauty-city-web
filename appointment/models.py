from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from accounts.models import Client
from beautycity_app.models import Employee, Service, Salon


class Appointment(models.Model):
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE, related_name='appointments', verbose_name='Салон')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='appointments', verbose_name='Клиент')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='appointments', verbose_name='Мастер')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Услуга')
    final_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Итоговая цена')
    promocode = models.CharField(max_length=255, null=True, blank=True, verbose_name='Промокод')
    comment = models.TextField(null=True, blank=True,verbose_name='Комментарий')
    date = models.DateField(verbose_name='Дата')
    start_time = models.TimeField(verbose_name='Время начала')
    end_time = models.TimeField(verbose_name='Конец')

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


class Review(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    master = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Мастер'
    )
    rating = models.DecimalField(max_digits=3, decimal_places=2,
                                 validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], verbose_name='Рейтинг')
    rating_img = models.ImageField(upload_to='img/reviews', null=True, blank=True, default='img/rating.svg',
                                   verbose_name='Изображение рейтинга')
    text = models.TextField(verbose_name='Отзыв')
    date = models.DateField(verbose_name='Дата')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
