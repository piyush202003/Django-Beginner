from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='RMPIndex'),
    path('login/', loginPage, name='RMPLogin'),
    path('register/', register, name='RMPRegister'),
    path('logout/', custom_logout, name='Logout'),
    path('editRecipe/<int:pk>', editRecipe, name='RMPEditRecipe'),
    path('deleteRecipe/<int:pk>', deleteRecipe, name='RMPDeleteRecipe'),
    path('pdf/', pdf, name='RMPPdf'),
]