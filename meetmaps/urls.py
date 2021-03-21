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
    path('event/<id>', views.event, name='event'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)