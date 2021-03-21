from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.forms import modelformset_factory

from .models import *

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['user']


class UserRegistrationForm(UserCreationForm):
    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError("The given email is already registered.")
        return self.cleaned_data['email']

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class CustomUserRegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['address']

class EventCreationForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'time', 'location_name',
            'description', 'address']

class EventDeletionForm(forms.ModelForm):
    class Meta:
        model = Event
        fields =[]