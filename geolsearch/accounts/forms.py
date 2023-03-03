from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):

    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control input_form flex','placeholder':' Имя пользователя'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control input_form flex','placeholder':' Пароль'}))

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control input_form flex', 'placeholder': ' Логин'}))
    first_name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form-control input_form flex', 'placeholder': ' Ваше имя'}))
    email = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form-control input_form flex', 'placeholder': 'E-mail'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control input_form flex', 'placeholder':' Пароль'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class': 'form-control input_form flex', 'placeholder':' Введите повторный пароль'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

