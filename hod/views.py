from django.http import HttpResponseRedirect
from django.shortcuts import render

from home.forms import AnnouncementForm
from home.models import Announcement
from django.contrib import messages

from members.models import *

# Create your views here.

def home(request):
    return render(request, 'home.html')


def add_announcement(request):
    form = AnnouncementForm(request.POST or None)
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        new = request.POST['new']
        if new == 'on':
            new = True
        else:
            new = False
        # date = request.POST['date']
        Announcement.objects.create(title=title, body=body, new=new)
        return HttpResponseRedirect('/add_announcement.html')
    else:
        return render(request, 'add_announcement.html', {'form': form})
    
def add_staff(request):
  return render(request, 'add_staff.html')

def do_add_staff(request):
  if request.method != 'POST':
    messages.success(request, 'Error adding staff. Please try again.')
    return HttpResponseRedirect('/hod/add_staff')
  else:
     first_name = request.POST['firstname']
     last_name = request.POST['lastname']
     email = request.POST['email']
     password = request.POST['password']
     address = request.POST['address']
     phone = request.POST['phone']
     username = request.POST['username']
     try:
      user = CustomUser.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password, username=username, user_type=2)
      user.staff.address = address
      user.staff.phone = phone
      user.save()
      messages.success(request, 'Staff added successfully!')
      return HttpResponseRedirect('/hod/add_staff')
     except:
      messages.success(request, 'Error adding staff. Please try again.')
      return HttpResponseRedirect('/hod/add_staff')

def add_course(request):
  # print(list(CustomUser.objects.values_list('email', flat=True).filter(user_type=1)))
  return render(request, 'add_course.html', {'emails': list(CustomUser.objects.values_list('email', flat=True).filter(user_type=1))})

def do_add_course(request):
  if request.method != 'POST':
    messages.success(request, 'Error adding course. Please try again.')
    return HttpResponseRedirect('/hod/add_course')
  else:
     name = request.POST['name']
     code = request.POST['code']
     adminEmail = request.POST['adminEmail']
     admin = Admin.objects.get(admin=CustomUser.objects.get(email=adminEmail))
     try:
      for sem in range(1,9):
        course = Course.objects.create(name=name, code=code,sem=sem, admin_id=admin)
      messages.success(request, 'Course added successfully!')
      return HttpResponseRedirect('/hod/add_course')
     except Exception as e:
      print(e)
      messages.success(request, 'Error adding course. Please try again.')
      return HttpResponseRedirect('/hod/add_course')