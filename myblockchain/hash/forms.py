from django import forms

class NewhashForm(forms.Form):
    data = forms.CharField(label='Input Data', max_length=100)

class NewblockForm(forms.Form):
    block_num = forms.CharField(label='Block Number', max_length=100)
    nonce = forms.CharField(label='Nonce', max_length=100)
    data = forms.CharField(label='Input Data', max_length=100)

class MineForm(forms.Form):
    block_num = forms.CharField(label='Block Number', max_length=100)
    nonce = forms.CharField(label='Nonce',disabled=True)
    data = forms.CharField(label='Input Data', max_length=100)