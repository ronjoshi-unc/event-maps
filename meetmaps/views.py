from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets, permissions
from django.contrib.auth.models import *
from django.contrib.auth import update_session_auth_hash
# from event.serializers import *
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib import messages
from meetmaps.forms import *
from meetmaps.models import *
from django.forms import modelformset_factory, formset_factory
from django.core.exceptions import ValidationError
from django.template.loader import render_to_string
from django.template import RequestContext
from django.http import JsonResponse
from django.core.mail import send_mail

import eventmaps
from notifications.signals import notify
from firebase import firebase
from django.http import HttpResponse
import itertools
import random


# Create your views here.
mapbox_access_token = 'pk.eyJ1Ijoia21nb3ZpbmQiLCJhIjoiY2ttaHZ2c2k1MGJkaDJ3cW90dzhzcDl3ZyJ9.8gnW35BhS9WSZaCBTOJ1IQ'

def home_page(request):
    page_title = 'Home'
    context = {'page_title' : page_title}
    return render(request, 'default.html', context)

def map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    page_title = 'Map'
    events = Event.objects.all()

    #Event creation form
    if request.method == "POST":
        eventCreationForm = EventCreationForm(request.POST)
        if eventCreationForm.is_valid():
            created = eventCreationForm.save(commit=False)
            created.host = request.user.customuser
            created.save()
        return redirect('/map')  
    else:
        eventCreationForm = EventCreationForm()

    context = { 'mapbox_access_token': mapbox_access_token, 'events' : events,  'eventCreationForm' : eventCreationForm}
    return render(request, 'map.html', context)

def event(request, id):
    event = Event.objects.get(id=id)
    page_title = Event.title

    context = {'mapbox_access_token': mapbox_access_token, 'page_title' : page_title, 'event' : event}
    return render(request, 'event.html', context)

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        custom_user_form = CustomUserRegistrationForm(request.POST)

        if user_form.is_valid() and custom_user_form.is_valid():
            user = user_form.save()
            email = user_form.cleaned_data['email']

            custom_user = custom_user_form.save(commit=False)

            custom_user.user = user
            custom_user.save()

            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('password')
            return redirect('/login/')
    else:
        user_form = UserRegistrationForm()
        custom_user_form = CustomUserRegistrationForm()
        
    context = {'user_form' : user_form, 'custom_user_form' : custom_user_form}
    return render(request, 'register.html', context)