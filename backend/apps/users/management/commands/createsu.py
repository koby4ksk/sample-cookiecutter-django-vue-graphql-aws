from django.core.management.base import BaseCommand

from apps.users.models import User


class Command(BaseCommand):
    help = 'Makes a superuser'

    def handle(self, *args, **options):
        superusers = User.objects.filter(email='test-name@example.com')
        if not superusers.exists():
            print('Super user is not in the database!')
        else:
            me = superusers.first()
            me.is_admin = True
            me.is_staff = True
            me.is_superuser = True
            me.save()
            print('Updated super user')
