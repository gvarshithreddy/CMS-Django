from django.shortcuts import render, loader
from django.contrib.auth import login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from members.EmailBackEnd import EmailBackEnd



# Create your views here.

def login_user(request):
    template = loader.get_template('login.html')
    context = {
        'login': False,
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        

        # authenticate user
        user = EmailBackEnd.authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in!')
            context['login'] = True
            return HttpResponseRedirect('/student/home')
            
        else:
            messages.success(request, 'Error logging in. Please try again.')
            return HttpResponseRedirect('/login')
    else:
        return HttpResponse(template.render(context, request))

def do_login(request):
    if request.method!='POST':
        messages.success(request, 'Error logging in. Please try again.')
        return HttpResponseRedirect('/login')
    else:
        email = request.POST['email']
        password = request.POST['password']
        user = EmailBackEnd.authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in!')
            if user.user_type == '1':
                return HttpResponseRedirect('/hod/home')
                # return HttpResponse("User is Admin")
            elif user.user_type == '2':
                return HttpResponseRedirect('/staff/home')
            elif user.user_type == '3':
                return HttpResponseRedirect('/student/home')
                # return HttpResponse('User is Student')
            
        else:
            messages.success(request, 'Error logging in. Please try again.')
            

    return HttpResponseRedirect('/login')

def logout_user(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return HttpResponseRedirect('/login')

def get_user_details(request):
    if request.user is not None:
        return HttpResponse("User: " + request.user.email + " usertype: " + request.user.user_type)
    else:
        return HttpResponse("Please Login First")
