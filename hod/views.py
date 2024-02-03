from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render

from home.forms import AnnouncementForm
from home.models import Announcement
from django.contrib import messages

from members.models import *

# Create your views here.

def home(request):
    course = list(set(Course.objects.filter(admin_id = request.user.admin.id)))[0]
    return render(request, 'home.html',{'course':course, 'user':request.user})


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
     
def add_student(request):
  # print(list(set(list(Course.objects.values_list('name', flat=True)))))
  return render(request, 'add_student.html', {'courses': list(set(list(Course.objects.values_list('code', flat=True)))), 'sems': range(1,9), 'start_years': range(datetime.now().year+1, datetime.now().year-10, -1), 'end_years': range(datetime.now().year+5, datetime.now().year-6, -1)})

def do_add_student(request):
  if request.method != 'POST':
    messages.success(request, 'Error adding student. Please try again.')
    return HttpResponseRedirect('/hod/add_student')
  else:
     first_name = request.POST['firstname']
     last_name = request.POST['lastname']
     email = request.POST['email']
     password = request.POST['password']
     roll_no = request.POST['rollno']
     gender = request.POST['gender']
     session_start_year = request.POST['session_start_year']
     session_end_year = request.POST['session_end_year']
     username = request.POST['username']
     code = request.POST['code']
     sem = request.POST['sem']
    #  try:
     print("I am here 1")
     user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=3)
     print("I am here 2")
     user.student.roll_no = roll_no
     user.student.gender = gender
     user.student.session_start_year = session_start_year
     user.student.session_end_year = session_end_year
     print("I am here 3")
     course_obj = Course.objects.get(code=code, sem=sem)
     if course_obj:
       print("Course is ",course_obj.name, " and sem is ",course_obj.sem)
       user.student.course = Course.objects.get(code=code, sem=sem)
     user.save()
     messages.success(request, 'Student added successfully!')
     return HttpResponseRedirect('/hod/add_student')
  #  except Exception as e:
     print(e)
     print("Course is ",Course.objects.get(code=code, sem=sem).name)
     messages.success(request, 'Error adding student. Please try again.')
     return HttpResponseRedirect('/hod/add_student')