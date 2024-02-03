from django.http import HttpResponseRedirect
from django.shortcuts import render

from home.forms import AnnouncementForm
from home.models import Announcement

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
        return HttpResponseRedirect('/announcements')
    else:
        return render(request, 'add_announcement.html', {'form': form})