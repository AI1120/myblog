from django import forms
from django.core import validators

#Dataflair #form
def check_size(value):
    if len(value)<6:
        raise forms.ValidationError('Password is too short')

class SignUp(forms.Form):
    first_name = forms.CharField(initial='First Name')
    last_name = forms.CharField()
    email = forms.EmailField(help_text='write your email')
    Adress = forms.CharField(required=False)
    Technology = forms.CharField(initial='Django', disabled=True)
    age = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput,),
    re_password = forms.CharField(help_text='renter your password',
                                  widget=forms.PasswordInput)
    botcatcher = forms.CharField(widget=forms.HiddenInput, required=False)
