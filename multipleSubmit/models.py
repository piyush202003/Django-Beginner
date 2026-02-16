from django.db import models

# Create your models here.
class MultipleSubmit(models.Model):
    subscription = [
        ('sub','subscribe'),
        ('unsub','unsubscribe'),
    ]
    email = models.EmailField()
    subscribe = models.CharField(choices=subscription)