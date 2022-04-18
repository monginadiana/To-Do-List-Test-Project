from django import forms
from django.db.models import fields
from django.forms import ModelForm

from .models import ToDo

class TodoForm(ModelForm):
    class Meta:
        model = ToDo
        fields = ['name', 'description', 'category', 'complete']

class updatetodoForm(ModelForm):
    class Meta:
        model = ToDo
        fields = ['name', 'description', 'category', 'complete']