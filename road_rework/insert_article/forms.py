from django import forms
from .models import *
from django.utils.timezone import now

class InsertAtricleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['article_id', 'date', 'article_name', 'content']
        widgets = {
            'article_id': forms.TextInput(attrs={'class': 'form-control input_form'}),
            'date': forms.DateInput(attrs={'class': 'form-control  input_form', 'type': 'date'}),
            'article_name': forms.TextInput(attrs={'class': 'form-control  input_form' , 'placeholder':'Название статьи'}),
            'content': forms.Textarea(attrs={'class': 'form-control  input_form_content' , 'type': 'text', 'placeholder':'текст'}),
        }
        labels = {
            'article_id': 'ID статьи',
            'date': 'Дата',
            'article_name': 'Название статьи:',
            'content': 'Текст статьи',
        }

    def __init__(self, *args, **kwargs):
        super(InsertAtricleForm, self).__init__(*args, **kwargs)
        self.fields['date'].initial = now