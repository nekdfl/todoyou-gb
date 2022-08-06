from django.core.management.base import BaseCommand
from authapp.management.common import cleardb

class Command(BaseCommand):

    """Удаляет комментарии, Статьи и пользователей"""
    def handle(self, *args, **options):
        cleardb()


