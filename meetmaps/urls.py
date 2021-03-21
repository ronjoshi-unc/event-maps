from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url                                                                                                                             
from . import views
from django.urls import path
urlpatterns = [ 
    path('', views.home_page, name='home'),
    path('map/', views.map, name='map'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('event/<id>', views.event, name='event'),
    path('events/', views.events, name='events'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)