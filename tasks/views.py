from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm()
        })
    else:
        if request.Post['password1'] == request.Post['password2']:
            user = User.objects.create_user(
                username=request.Post['username'],
                password=request.Post['password1']
            )
        return HttpResponse('Password did not match')