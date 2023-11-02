from django.shortcuts import render, redirect
from django.urls import reverse
import json
from rest_framework.views import Response

from rest_framework.decorators import api_view
from .serializer import UserSerializer
from django.contrib.auth import login, authenticate
def browser_client(request):
   return render(request, 'product/client.html')

def login_view(request):
    dt = request.POST
    user = authenticate(username=dt['username'], password=dt['password'])
    if user is not None:
        login(request, user)
        return redirect(reverse('djclient'))
    
    return Response({'message': 'username or password invalid'}, status=404)