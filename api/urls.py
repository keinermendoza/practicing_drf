from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views
urlpatterns = [
    path('', views.product, name='product'),
    path('auth/', obtain_auth_token, name='auth')

]
