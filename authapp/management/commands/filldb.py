from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from authapp.management.common import create_admin_user, create_users


class Command(BaseCommand):

    def handle(self, *args, **options):
        """Fill DB with testdata """
        print("Create users")
        create_admin_user(username="admin", password="admin")
        create_users(5)





