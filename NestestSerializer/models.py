from django.db import models

# Create your models here.
class GFG(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.ForeignKey(GFG, on_delete=models.CASCADE)
    item = models.CharField(max_length=50)
    def __str__(self):
        return f'name={self.name}, item={self.item}'