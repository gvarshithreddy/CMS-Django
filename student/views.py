from django.shortcuts import render
from home.models import Announcement
from members.models import Student, NotificationStudent

# Create your views here.

def studentHome(request):
    context = {
        'announcements': Announcement.objects.all().order_by('-date'),
        'Nnotifications': NotificationStudent.objects.all().order_by('-created_at')[:5],
    }
    print(context)
    return render(request, 'studentHome.html', context)
