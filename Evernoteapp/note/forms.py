from django import forms
from django.forms import ModelForm
from .models import note

class Noteform(forms.ModelForm):
    class Meta:
        model = note
        fields ='__all__'
