from datetime import datetime, time
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.defaulttags import register

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
     try:
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
     except Exception as e:
      print(e)
      print("Course is ",Course.objects.get(code=code, sem=sem).name)
      messages.success(request, 'Error adding student. Please try again.')
      return HttpResponseRedirect('/hod/add_student')


def add_subject(request):
  return render(request, 'add_subject.html', {'courses': list(set(list(Course.objects.values_list('code', flat=True))) ), 'sems': range(1,9)})

def do_add_subject(request):
  if request.method != 'POST':
    messages.success(request, 'Error adding subject. Please try again.')
    return HttpResponseRedirect('/hod/add_subject')
  else:
     name = request.POST['name']
     code = request.POST['code']
     course_code = request.POST['course_code']
     sem = request.POST['sem']
     try:
      course = Course.objects.get(code=course_code, sem = sem)
      subject = Subject.objects.create(name=name, code=code, course_id=course)
      messages.success(request, 'Subject added successfully!')
      return HttpResponseRedirect('/hod/add_subject')
     except:
      messages.success(request, 'Error adding subject. Please try again.')
      return HttpResponseRedirect('/hod/add_subject')

def add_course_schedule(request):
  return render(request, 'add_course_schedule.html', {'courses': list(set(list(Course.objects.values_list('code', flat=True))) ), 'sems': range(1,9), 'days': {"Monday":0,  "Tuesday":1, "Wednesday":2, "Thursday":3, "Friday":4, "Saturday":5, "Sunday":6}, 'start_times': [time(9,10).strftime("%I:%M"),time(10,10).strftime("%I:%M"), time(11,15).strftime("%I:%M"), time(13,0).strftime("%I:%M"), time(14,0).strftime("%I:%M"), time(15,0).strftime("%I:%M")], 'end_times': [time(10,10).strftime("%I:%M"),time(11,10).strftime("%I:%M"), time(12,15).strftime("%I:%M"), time(14,0).strftime("%I:%M"), time(15,0).strftime("%I:%M"), time(16,0).strftime("%I:%M")], 'staffs': list(CustomUser.objects.filter(user_type=2)), 'subjects': list(Subject.objects.values_list('name', flat=True))})

def do_add_course_schedule(request):
  days= {"Monday":0,  "Tuesday":1, "Wednesday":2, "Thursday":3, "Friday":4, "Saturday":5, "Sunday":6}
  start_times = [time(9,10).strftime("%I:%M"),time(10,10).strftime("%I:%M"), time(11,15).strftime("%I:%M"), time(13,0).strftime("%I:%M"), time(14,0).strftime("%I:%M"), time(15,0).strftime("%I:%M")]
  if request.method != 'POST':
    messages.success(request, 'Error adding course schedule. Please try again.')
    return HttpResponseRedirect('/hod/add_course_schedule')
  else:
     course_code = request.POST['course_code']
     sem = request.POST['sem']
    #  day = request.POST['day']
    #  start_time = request.POST['start_time']
    #  end_time = request.POST['end_time']
     staff_id = request.POST['staff']
    #  subject_name = request.POST['subject']

     for day in days:
      for start_time in start_times:
        schedule = request.POST[day+"_"+start_time]
        print("Schedule is ",schedule, "on", day, "at", start_time)

     return HttpResponseRedirect('/hod/add_course_schedule')
    # #  try:
    #  course = Course.objects.get(code=course_code, sem = sem)
    #  staff = Staff.objects.get(id = staff_id)
    #  subject = Subject.objects.get(name=subject_name)
    #  schedule = ScheduleStudent.objects.create(course_id=course, day=day, start_time=start_time, end_time=end_time, staff_id=staff, subject_id=subject)
    #  messages.success(request, 'Course schedule added successfully!')
    #  return HttpResponseRedirect('/hod/add_course_schedule')
    # #  except:
    #  messages.success(request, 'Error adding course schedule. Please try again.')
    #  return HttpResponseRedirect('/hod/add_course_schedule')
     
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)