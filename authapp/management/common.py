import random

from authapp.models import User
from random_username.generate import generate_username
# from django.db.models import Max

def cleardb():
    pass
    User.objects.all().delete()


def create_admin_user(username, password):
    admin = User.objects.create_user(username=username, password=password)
    admin.is_superuser = True
    admin.is_staff = True
    admin.is_active = True
    admin.email = f"{username}@host.ru"
    admin.save()
    print(f"Super user credential {username}:{password}")


def create_users(count):
    '''Создает пользователей со случаныйными именами в колличестве count'''
    usernames = generate_username(count)
    for name in usernames:
        password = f"{name}-password"
        email = f"{name}@host.ru"
        user = User.objects.create_user(username=name, password=password, email=email)
        user.save()
        print(f"Single user credential {name}:{password}")

