from django import forms
from .models import *

class BlogForm(forms.ModelForm):
    """Form definition for Blog."""

    class Meta:
        """Meta definition for Blogform."""

        model = Blog
        fields = ('name', 'description', 'image', )
