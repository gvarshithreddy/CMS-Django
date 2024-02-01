from django.shortcuts import render, loader
from django.http import HttpResponse
from .models import Announcement

# Create your views here.

def home(request):
    return render(request, 'main.html')

def announcements(request):
    template = loader.get_template('announcements.html')
    context = {
        'announcements': Announcement.objects.all().order_by('-date'),
    }

    return HttpResponse(template.render(context, request))
