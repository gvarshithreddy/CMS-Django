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
    course = list(set(Course.objects.filter(admin_id = request.user.admin.id)))
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
  courses = list(set(list(Course.objects.values_list('code', flat=True).order_by('code'))))
  return render(request, 'add_subject.html', {'courses': courses , 'sems': range(1,9)})

def do_add_subject(request):
  if request.method != 'POST':
    messages.success(request, 'Error adding subject. Please try again.')
    return HttpResponseRedirect('/hod/add_subject')
  else:
     name = request.POST['name']
     code = request.POST['code']
     coursesList = list(map(str,request.POST['selectedCourses'].strip().split(',')))
     print(coursesList)
     sem = request.POST['sem']
     try:
      subject = Subject.objects.create(name=name, code=code)
      for coursecode in coursesList:
        course = Course.objects.get(code=coursecode, sem=sem)
        subject.course_id.add(course)
      messages.success(request, 'Subject added successfully!')
      return HttpResponseRedirect('/hod/add_subject')
     except:
      messages.success(request, 'Error adding subject. Please try again.')
      return HttpResponseRedirect('/hod/add_subject')

def add_course_schedule(request):
  start_times = [time(9,10).strftime("%I:%M"),time(10,10).strftime("%I:%M"), time(11,15).strftime("%I:%M"), time(13,0).strftime("%I:%M"), time(14,0).strftime("%I:%M"), time(15,0).strftime("%I:%M")]
  end_times= [time(10,10).strftime("%I:%M"),time(11,10).strftime("%I:%M"), time(12,15).strftime("%I:%M"), time(14,0).strftime("%I:%M"), time(15,0).strftime("%I:%M"), time(16,0).strftime("%I:%M")]
  times = zip(start_times, end_times)
  context = {
    'courses': list(set(list(Course.objects.values_list('code', flat=True))) ), 
    'sems': range(1,9), 
    'days': {"Monday":0,  "Tuesday":1, "Wednesday":2, "Thursday":3, "Friday":4, "Saturday":5}, 
    'times':times,
    'staffs': list(CustomUser.objects.filter(user_type=2)), 'subjects': list(Subject.objects.values_list('name', flat=True)),
    }
  
  return render(request, 'add_course_schedule.html', context)

# def do_add_course_schedule(request):
#   days= {"Monday":0,  "Tuesday":1, "Wednesday":2, "Thursday":3, "Friday":4, "Saturday":5, "Sunday":6}
#   start_times = [time(9,10).strftime("%I:%M"),time(10,10).strftime("%I:%M"), time(11,15).strftime("%I:%M"), time(13,0).strftime("%I:%M"), time(14,0).strftime("%I:%M"), time(15,0).strftime("%I:%M")]
#   end_times= [time(10,10).strftime("%I:%M"),time(11,10).strftime("%I:%M"), time(12,15).strftime("%I:%M"), time(14,0).strftime("%I:%M"), time(15,0).strftime("%I:%M"), time(16,0).strftime("%I:%M")]
#   times = zip(start_times, end_times)
#   from django.shortcuts import render, redirect
# from .models import ScheduleStudent
def add_schedule_student(request,day_index, start_time, end_time, course_code, semester):
  days= {"Monday":0,  "Tuesday":1, "Wednesday":2, "Thursday":3, "Friday":4, "Saturday":5, "Sunday":6}

  subject_name = request.POST.get(f'{day_index}_{start_time}_{end_time}_subject')
  staff_id = request.POST.get(f'{day_index}_{start_time}_{end_time}_staff')

  # Create or update schedule
  schedule, _ = ScheduleStudent.objects.update_or_create(
      course_id=Course.objects.get(code=course_code, sem = semester),
      # semester=semester,
      day=days[day_index],
      start_time=start_time,
      end_time=end_time,
      defaults={
          'subject_id': Subject.objects.get(name=subject_name),
          'staff_id': Staff.objects.get(id=staff_id),
          'status': False,  # Assuming status should be set to False for new schedules
      }
  )


def do_add_course_schedule(request):
    start_times = [time(9,10).strftime("%I:%M"),time(10,10).strftime("%I:%M"), time(11,15).strftime("%I:%M"), time(13,0).strftime("%I:%M"), time(14,0).strftime("%I:%M"), time(15,0).strftime("%I:%M")]
    end_times= [time(10,10).strftime("%I:%M"),time(11,10).strftime("%I:%M"), time(12,15).strftime("%I:%M"), time(14,0).strftime("%I:%M"), time(15,0).strftime("%I:%M"), time(16,0).strftime("%I:%M")]
    # times = zip(start_times, end_times)
    days= {"Monday":0,  "Tuesday":1, "Wednesday":2, "Thursday":3, "Friday":4, "Saturday":5, "Sunday":6}

    if request.method == 'POST':
        # Extract data from the form
        course_code = request.POST.get('course_code')
        semester = request.POST.get('sem')

        # Iterate over the form fields to extract schedule data
        count = 0
        # print(times)
        for day_index in days:
            count+=1
            iter = 0
            while iter < len(start_times):
              start_time = start_times[iter]
              end_time = end_times[iter]
              iter+=1
              add_schedule_student(request,day_index, start_time, end_time, course_code, semester)
                

        # Redirect to a success page or to the same page with a success message
        messages.success(request, 'Course schedule added successfully!')
        return HttpResponseRedirect('/hod/add_course_schedule/')  # You should define a URL pattern named 'success_page' for this to work

    # If request method is not POST, render the form page again
    messages.success(request, 'Error adding course schedule. Please try again.')
    return HttpResponseRedirect('/hod/add_course_schedule/')  # Replace 'your_template.html' with the name of your template file

def view_leave_requests(request):
  context ={
    'studentLeaves': LeaveReportStudent.objects.all(),
    'staffLeaves': LeaveReportStaff.objects.all(),
    'days': {"hi":1}
  }
  return render(request, 'view_leave_requests.html', context=context)
     
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def get_student_rollno(dictionary, id):
    return Student.objects.get(id=id).roll_no


@register.filter
def get_student_course(dictionary, id):
    return Student.objects.get(id=id).course.name

@register.filter
def get_staff_name(dictionary, id):
    return CustomUser.objects.get(id=Staff.objects.get(id=id).admin_id).first_name