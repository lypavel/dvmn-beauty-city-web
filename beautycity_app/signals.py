from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import EmployeeSchedule


@receiver(post_save, sender=EmployeeSchedule)
def check_employee_in_salon(sender, instance, **kwargs):
    if not instance.salon.masters.filter(id=instance.employee.id).exists():
        raise ValueError(f"Мастер {instance.employee.name} не работает в салоне {instance.salon.title}.")
