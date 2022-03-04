from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from  phonenumber_field.modelfields import PhoneNumberField

class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")


    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")