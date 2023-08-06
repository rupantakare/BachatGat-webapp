from django import forms
from django.contrib.auth.models import User
from .models import Userprofile

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Userprofile
        fields = ['name', 'account_no', 'aadhar_no', 'pan_no', 'email', 'mobile', 'username', 'password', 'birthday','address','city','state','zip']