from django import forms
from .models import Todo

class TodoItem(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'reminder']

class ShareTaskForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['shared_with'] 
