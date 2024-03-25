from django.contrib.auth import views as auth_views
from django.urls import path 

from . import views 
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto/', views.contact, name='contact'),
    path('registro/', views.signup, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login')
]

