from django.urls import path
from . import views

urlpatterns = [
  path ('home/', views.studentHome, name='studentHome'),
  # path ('add_staff/', views.add_staff, name='add_staff'),
  path ('schedule/', views.studentSchedule, name='studentSchedule'),
  path ('apply_leave/', views.studentApplyLeave, name='studentApplyLeave'),
  path('do_apply_leave/', views.do_studentApplyLeave, name = 'do_studentApplyLeave')
]