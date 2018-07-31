from django.shortcuts import render

# Create your views here.
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...
def logout(request):
    logout(request)
    # Redirect to a success page.