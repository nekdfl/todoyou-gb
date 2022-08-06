import base64
import os

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
def get_b64_avatr_filename(filename, user_pk):
    file_ext = str(filename).split(".")[-1]
    new_filename = base64.urlsafe_b64encode(f'user-{user_pk}'.encode('ascii')).decode('ascii')
    return f'{new_filename}.{file_ext}'


def delete_old_photo(filename, user_pk):
    upload_dir = "user_avatar"
    file_ext = str(filename).split(".")[-1]
    new_filename = base64.urlsafe_b64encode(f'user-{user_pk}'.encode('ascii')).decode('ascii')
    filepath = os.path.join(upload_dir, f'{new_filename}.{file_ext}')
    os.remove(filepath)


def upload_avatar(instance, filename):
    upload_dir = "user_avatar"
    if os.path.exists(os.path.join(upload_dir, str(instance.image))):
        delete_old_photo(instance.image, instance.pk)
    return os.path.join(upload_dir, f'{get_b64_avatr_filename(filename, instance.pk)}')


class User(AbstractUser):
    pass
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to=upload_avatar, blank=True)
