from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [ 
    path('', views.home_page, name='home'),
    path('map/', views.map, name='map'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('event/<id>', views.event, name='event'),
]