from django.shortcuts import render, redirect
from django.urls import reverse
import json
from rest_framework.views import Response

from rest_framework.decorators import api_view
from .serializer import UserSerializer
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login-client/')
def browser_client(request):
   return render(request, 'djclient/client.html')

def logout_client(request):
    logout(request)
    return redirect(reverse('djclient'))

def login_client(request):
    if request.method == 'POST':

        dt = request.POST
        user = authenticate(username=dt['username'], password=dt['password'])

        if user is not None:
            login(request, user)
            return redirect(reverse('djclient'))
        
        return render(request, 'djclient/login.html', {'message': 'User not valid'})
    return render(request, 'djclient/login.html', {'message': 'wellcome to the login page'})

