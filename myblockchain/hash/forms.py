from django import forms

class NewhashForm(forms.Form):
    data = forms.CharField(label='data', max_length=100)
