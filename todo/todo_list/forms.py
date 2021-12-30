from .models import List
from django import forms

class Listform(forms.ModelForm):
    class Meta:
        model = List
        fields = ["item","completed"]

