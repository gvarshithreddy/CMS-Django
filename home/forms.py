from django import forms
from django.forms import ModelForm
from .models import Announcement
from django.contrib.admin.widgets import AdminDateWidget

class AnnouncementForm(ModelForm):
  class Meta:
    model = Announcement
    fields = ['title', 'new', 'body']
    # widgets = {
    #   'date': forms.DateInput(attrs={'type': 'date'}),
    # }
    labels = {
      'title': 'Title',
      'new': 'New',
      'body': 'Body',
      # 'date': 'Date',
    }
    help_texts = {
      'title': 'Enter the title of the announcement.',
      'new': 'Check this box if this is a new announcement.',
      'body': 'Enter the body of the announcement.',
      # 'date': 'Enter the date of the announcement.',
    }
    error_messages = {
      'title': {
        'max_length': "This title is too long.",
      },
    }