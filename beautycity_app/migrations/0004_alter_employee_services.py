# Generated by Django 4.2.13 on 2024-07-28 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beautycity_app', '0003_alter_employeeschedule_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='services',
            field=models.ManyToManyField(related_name='employees', to='beautycity_app.service', verbose_name='Услуги'),
        ),
    ]
