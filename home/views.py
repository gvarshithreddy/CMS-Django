from django.shortcuts import render, loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import Announcement
from .forms import AnnouncementForm

# Create your views here.

def home(request):
    return render(request, 'main.html')

def announcements(request):
    template = loader.get_template('announcements.html')
    context = {
        'announcements': Announcement.objects.all().order_by('-date'),
    }

    return HttpResponse(template.render(context, request))

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
        return HttpResponseRedirect('/announcements')
    else:
        return render(request, 'add_announcement.html', {'form': form})
