from django.shortcuts import render
from django.contrib.auth import authenticate, login, user_logged_out
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages



# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in!')
            return HttpResponseRedirect('/')
        else:
            messages.error(request, 'Error logging in. Please try again.')
            return HttpResponseRedirect('/login')
    else:
        return render(request, 'login.html')
