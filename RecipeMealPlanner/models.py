from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Plans(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank= True)
    day = models.CharField(max_length=100, default='something')
    name = models.CharField(max_length=100, default='something')
    description = models.TextField(max_length=1000, default='something')

    def __str__(self):
        return f'{User.username} have recepie {self.name} at the day {self.day}'