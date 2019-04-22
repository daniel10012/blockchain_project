from django import forms

class NewhashForm(forms.Form):
    data = forms.CharField(label='data', max_length=100)
    hashed_data = forms.CharField(label='hashed_data', max_length=100)