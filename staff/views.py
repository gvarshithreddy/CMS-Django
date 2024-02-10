from datetime import time
from django.shortcuts import render
from django.template.defaulttags import register
from members.models import *
from django.http import HttpResponse, HttpResponseRedirect, request

# Create your views here.
staff_id = 1


def staffHome(request):
    return render(request, 'staffHome.html')

def staffSchedule(request):
    global staff_id
    start_times = [time(9,10).strftime("%I:%M"),time(10,10).strftime("%I:%M"), time(11,15).strftime("%I:%M"), time(13,0).strftime("%I:%M"), time(14,0).strftime("%I:%M"), time(15,0).strftime("%I:%M")]
    end_times= [time(10,10).strftime("%I:%M"),time(11,10).strftime("%I:%M"), time(12,15).strftime("%I:%M"), time(14,0).strftime("%I:%M"), time(15,0).strftime("%I:%M"), time(16,0).strftime("%I:%M")]
    times = zip(start_times, end_times)
    days = {"0": "Monday", "1": "Tuesday", "2": "Wednesday", "3": "Thursday", "4": "Friday", "5": "Saturday"}
    nums = [0,1,2,3,4,5]
    staff_id = request.user.staff.id
    staff_schedules = ScheduleStudent.objects.filter(staff_id_id=request.user.staff.id).order_by('day')
    first_schedule = []
    second_schedule = []
    third_schedule = []
    fourth_schedule = []
    fifth_schedule = []
    sixth_schedule = []
    for staff_schedule in staff_schedules:
        # print(staff_schedule.start_time, days[str(staff_schedule.day)])
        if staff_schedule.start_time == time(9,10):
            first_schedule.append(staff_schedule)
        elif staff_schedule.day == time(10,10):
            second_schedule.append(staff_schedule)
        elif staff_schedule.day == time(11,15):
            third_schedule.append(staff_schedule)
        elif staff_schedule.day == time(13,0):
            fourth_schedule.append(staff_schedule)
        elif staff_schedule.day == time(14,0):
            fifth_schedule.append(staff_schedule)
        elif staff_schedule.day == time(15,0):
            sixth_schedule.append(staff_schedule)
    
    context = {
        'days': days,
        'times': times,
        'first_schedule': first_schedule,
        'second_schedule': second_schedule,
        'third_schedule': third_schedule,
        'fourth_schedule': fourth_schedule,
        'fifth_schedule': fifth_schedule,
        'sixth_schedule': sixth_schedule,
        'nums': nums,
        'staff_schedules': staff_schedules,
    }
        
    


    return render(request, 'view_schedule_staff.html', context=context )
@register.filter
def get_subject_staff(day, start_time):
    global staff_id
    print(staff_id)
    h,m = map(int, start_time.split(':'))
    start_time1 = time(h,m)
    try:
        return ScheduleStudent.objects.get(day = day, start_time = start_time1, staff_id_id= staff_id).subject_id.name
    except:
        return "Error"


@register.filter
def get_day(days, day):
    return days.get(day)