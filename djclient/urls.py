from django.urls import path
from . import views

urlpatterns = [
    path('', views.browser_client, name='djclient'),
    path('login-client/', views.login_client, name='login_client'),
    path('logout-client/', views.logout_client, name='logout_client'),

    
]
