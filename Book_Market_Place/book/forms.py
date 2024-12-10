from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class signup_Form(UserCreationForm):
    username = forms.CharField(widget= forms.TextInput(attrs={'class':' w-full py-2 px-2 mt-2 rounded-xl','placeholder':'Enter Your Name'}),label='UserName')
    email = forms.CharField(widget= forms.EmailInput(attrs={'class':' w-full py-2 px-2 mt-2 rounded-xl','placeholder':'Email'}),label='Email')
    password1 = forms.CharField(widget= forms.PasswordInput(attrs={'class':' w-full py-2 px-2 mt-2 rounded-xl','placeholder':'Enter your Password'}),label='Password')
    password2 = forms.CharField(widget= forms.PasswordInput(attrs={'class':'w-full py-2 px-2 mt-2 rounded-xl','placeholder':'Confirm Password'}),label='Confirm Password')
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']