from django import forms
from .models import TodoModel

class TodoModelForm(forms.ModelForm):
    class Meta:
        model = TodoModel
        exclude = ["id"]
        widgets = {
            'status': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'タイトル...'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '内容...'}),
        }
        labels = {
            'title': 'タイトル',
            'content': '内容',
            'status': 'ステータス'
        }