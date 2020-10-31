from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput,EmailInput,NumberInput
from .models import User


class UserSignupForm(UserCreationForm):
    password1 = forms.CharField(
        label= ("Password"),
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'required': 'true',

                                          }),
        help_text = ("Your password cant be too similar to your other personal information,cant be a commonly used password,cant be entirely numeric and must contain atleast 8 characters")
    )
    password2 = forms.CharField(
        label= ("Password confirmation"),
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'type': 'password',
                                          'required': 'true',
                                          }),
        help_text= ("Enter the same password as above, for verification.")
    )
    class Meta():
        model = User
        fields = ['first_name','last_name','email','password1','password2']
        widgets = {
            'first_name': TextInput(attrs={
                'class': 'form-control'
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Provide a valid email address',
                'required':'true'
            }),

        }