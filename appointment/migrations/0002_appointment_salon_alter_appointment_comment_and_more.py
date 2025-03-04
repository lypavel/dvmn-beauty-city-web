# Generated by Django 4.2.13 on 2024-07-26 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beautycity_app', '0002_alter_employee_photo_alter_employee_rating_img_and_more'),
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='salon',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='beautycity_app.salon', verbose_name='Салон'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='promocode',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Промокод'),
        ),
    ]
