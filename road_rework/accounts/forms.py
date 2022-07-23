from django import forms

class LoginForm(forms.Form):

    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'integer','placeholder':' Имя пользователя'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':' Пароль'}))
