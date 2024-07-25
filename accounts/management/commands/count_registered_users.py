import sys

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Count registered clients (except superusers and staff)'

    def handle(self, *args, **kwargs):
        User = get_user_model()

        print(
            'Clients registered:',
            User.objects.filter(is_superuser=False, is_staff=False).count(),
            file=sys.stdout
        )
