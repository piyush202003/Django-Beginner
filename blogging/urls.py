from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name='bloggingIndex'),
    path('<int:pk>',blogDetails, name='blogDetails'),
    path('create/', createBlog, name='createBlog'),
    path('edit/<int:pk>', editBlog, name='editBlog'),
    path('del/<int:pk>', deleteBlog, name='deleteBlog'),
]