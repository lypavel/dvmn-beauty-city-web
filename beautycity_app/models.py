from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from .model_fields import ImageAndSvgField


class Salon(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    masters = models.ManyToManyField('Employee', related_name='salons', verbose_name='Мастера')
    img = ImageAndSvgField(upload_to='img/salons', null=True, blank=True, verbose_name='Изображение')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Салон'
        verbose_name_plural = 'Салоны'

    def __str__(self):
        return self.title


class Service(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, max_length=255, verbose_name='Категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(100)],
                                verbose_name='Цена')
    duration = models.DurationField(help_text="Продолжительность услуги в формате ЧЧ:ММ:СС",
                                    verbose_name='Длительность')
    img = ImageAndSvgField(upload_to='img/services', null=True, blank=True, verbose_name='Изображение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    position = models.CharField(max_length=255, verbose_name='Специализация')
    services = models.ManyToManyField(Service, verbose_name='Услуги', related_name='employees')
    rating = models.DecimalField(max_digits=3, decimal_places=2,
                                 validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], verbose_name='Рейтинг')
    rating_img = ImageAndSvgField(upload_to='img/employees', null=True, blank=True, default='img/rating.svg',
                                   verbose_name='Изображение рейтинга')
    experience = models.CharField(max_length=255, verbose_name='Опыт')
    photo = ImageAndSvgField(upload_to='img/masters', default='img/masters/all.svg', null=True, blank=True,
                              verbose_name='Фото')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'

    def __str__(self):
        return self.name


class EmployeeSchedule(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Мастер', related_name='schedule')
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE, verbose_name='Салон')
    date = models.DateField(verbose_name='Дата')
    start_time = models.TimeField(verbose_name='Начало работы')
    end_time = models.TimeField(verbose_name='Конец работы')

    def __str__(self):
        return f'{self.date} - {self.employee.name} - {self.salon.title}'

    class Meta:
        verbose_name = 'Расписание мастера'
        verbose_name_plural = 'Расписания мастеров'

    def __str__(self):
        return f'{self.employee} - {self.date} - {self.start_time}'


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория услуг'
        verbose_name_plural = 'Категории услуг'

    def __str__(self):
        return self.title
