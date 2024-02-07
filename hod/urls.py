from django.urls import path
from . import views

urlpatterns = [
  path ('home/', views.home, name='hodHome'),
  path ('add_announcement/', views.add_announcement, name='add_announcement'),
  path ('add_staff/', views.add_staff, name='add_staff'),
  path ('do_add_staff/', views.do_add_staff, name='do_add_staff'),
  path ('add_course/', views.add_course, name='add_course'),
  path ('do_add_course/', views.do_add_course, name='do_add_course'),
  path ('add_student/', views.add_student, name='add_student'),
  path ('do_add_student/', views.do_add_student, name='do_add_student'),
  path ('add_subject/', views.add_subject, name='add_subject'),
  path ('do_add_subject/', views.do_add_subject, name='do_add_subject'),
  path ('add_course_schedule/', views.add_course_schedule, name='add_course_schedule'),
  path ('do_add_course_schedule/', views.do_add_course_schedule, name='do_add_course_schedule'),
]