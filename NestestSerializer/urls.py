from django.urls import path
from .views import *

urlpatterns = [
    path('get-data/', index, name='NestestSerializerIndex'),
]