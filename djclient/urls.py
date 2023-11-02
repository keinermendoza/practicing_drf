from django.urls import path
from . import views

urlpatterns = [
    path('', views.browser_client, name='djclient'),
    path('login', views.login_view, name='browser_login'),
]
