from django.urls import path
from . import views

urlpatterns = [
  path('home/', views.staffHome, name='staffHome'),
  path('schedule/', views.staffSchedule, name='staffSchedule'),
]