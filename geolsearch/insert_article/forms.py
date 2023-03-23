from django import forms

class UserSearch(forms.Form):
    text = forms.CharField(max_length=100)
    tag = forms.CharField(max_length=100)
    table = forms.CharField(max_length=100)


