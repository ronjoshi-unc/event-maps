from django.conf.urls import url
from django.urls import path                                                                                                                              
from . import views

urlpatterns = [ 
    path('', views.home_page, name='home'),
    path('map/', views.map, name='map'),
    path('events/', views.events, name='events'),
]