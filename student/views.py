from datetime import time
from django.http import HttpResponse
from django.shortcuts import render
from home.models import Announcement
from members.models import *
from django.template.defaulttags import register

# Create your views here.

def studentHome(request):
    context = {
        'announcements': Announcement.objects.all().order_by('-date'),
        'Nnotifications': NotificationStudent.objects.all().order_by('-created_at')[:5],
    }
    print(context)
    return render(request, 'studentHome.html', context)

def studentSchedule(request):
    course_id = 2
    start_times= [time(9,10).strftime("%I:%M"),time(10,10).strftime("%I:%M"), time(11,15).strftime("%I:%M"), time(13,0).strftime("%I:%M"), time(14,0).strftime("%I:%M"), time(15,0).strftime("%I:%M")]
    end_times= [time(10,10).strftime("%I:%M"),time(11,10).strftime("%I:%M"), time(12,15).strftime("%I:%M"), time(14,0).strftime("%I:%M"), time(15,0).strftime("%I:%M"), time(16,0).strftime("%I:%M")]
    times= zip(start_times, end_times)
    context = {
        'schedules': ScheduleStudent.objects.filter(course_id=course_id).order_by('day'),
        'days': {'0': 'Monday', '1': 'Tuesday', '2': 'Wednesday', '3': 'Thursday', '4': 'Friday', '5': 'Saturday',},
        'times':times,
        
        
    }
    
    return render(request, 'view_student_schedule.html', context=context)

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def get_subject(day, start_time):
    h,m = map(int, start_time.split(':'))
    start_time1 = time(h,m)
    print(start_time1)
    # print(start_time)
    try:
       return ScheduleStudent.objects.get(day = day, start_time = start_time1).subject_id.name
    except:
       return "Error"