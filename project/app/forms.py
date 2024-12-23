from django import forms
from .models import Evaluation, Personnel

class PersonnelForm(forms.ModelForm):
    class Meta:
        model = Personnel
        fields = '__all__'

class EvaluationForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = ['evaluation_type', 'criteria', 'performance_rating', 'skills_developed', 'comments']
    
    # Customize criteria as a JSON field (could be a formset or a dynamic form in the frontend)
    criteria = forms.CharField(widget=forms.Textarea, required=False)
