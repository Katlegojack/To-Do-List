from .models import Task
from django import forms
from django.forms import ModelForm

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add in a new task: '}))

    class Meta:
        model = Task
        fields = "__all__"
        
