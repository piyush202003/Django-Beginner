from django import forms
from .models import ToDoList

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = '__all__'
