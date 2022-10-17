"""way to add and edit entries;
create a new form from scratch or use "ModelForm" to save form content to model
"""
from django import forms
# import django forms

from .models import Post
# import model Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)
