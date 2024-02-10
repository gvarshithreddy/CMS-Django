from django.urls import path
from . import views

urlpatterns = [
  path('home/', views.staffHome, name='staffHome'),
  path('schedule/', views.staffSchedule, name='staffSchedule'),
  path('apply_leave/', views.staffApplyLeave, name='staffApplyLeave'),
  path ('do_apply_leave/', views.do_staffApplyLeave, name='do_staffApplyLeave')
]