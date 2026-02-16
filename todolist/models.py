from django.db import models
from django.utils import timezone

# Create your models here.
class ToDoList(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default="There is no description")
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        # return super().__str__(self.title)
        return self.title
    