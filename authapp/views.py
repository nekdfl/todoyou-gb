from django.shortcuts import render

# Create your views here.
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet

from authapp.models import User
from authapp.serializers import UserModelSerializer


class UserModelViewSet(ModelViewSet):
    # renderer_classes = [JSONRenderer]
    queryset = User.objects.all()
    serializer_class = UserModelSerializer