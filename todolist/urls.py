from django.urls import path
from .views import *

urlpatterns = [
    path('', index , name = 'todolistIndex'),
    path('del/<int:id>', deleteList, name='deleteTodo'),
]
