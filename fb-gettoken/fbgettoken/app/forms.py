from django import forms

class SimpleForm(forms.Form):
    user = forms.CharField(label='Username', max_length=100)
    passwd = forms.CharField(label='Password', widget=forms.PasswordInput)