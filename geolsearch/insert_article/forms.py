from django import forms

class UserSearch(forms.Form):
    text = forms.CharField(max_length=100, required=False)
    tag = forms.CharField(max_length=100, required=False)
    table = forms.CharField(max_length=100, required=False  )


class FacetedSearch(forms.Form):
    textS = forms.CharField(max_length=100)
    tagS = forms.CharField(max_length=100)
    tableS = forms.CharField(max_length=100)



