# forms.py
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'completed', 'priority']

    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    due_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}))
    completed = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    priority = forms.ChoiceField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')],
                                 widget=forms.Select(attrs={'class': 'form-control'}))
