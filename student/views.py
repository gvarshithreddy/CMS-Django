from django.shortcuts import render
from home.models import Announcement

# Create your views here.

def studentHome(request):
    context = {
        'announcements': Announcement.objects.all().order_by('-date'),
    }
    print(context)
    return render(request, 'studentHome.html', context)
