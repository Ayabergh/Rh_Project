from django import forms
from .models import Personnel

class PersonnelForm(forms.ModelForm):
    class Meta:
        model = Personnel
        fields = '__all__'
