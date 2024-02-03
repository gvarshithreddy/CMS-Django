from django.urls import path
from . import views

urlpatterns = [
  path ('home/', views.home, name='hodHome'),
  path ('add_announcement/', views.add_announcement, name='add_announcement'),
  path ('add_staff/', views.add_staff, name='add_staff'),
  path ('do_add_staff/', views.do_add_staff, name='do_add_staff'),
  path ('add_course/', views.add_course, name='add_course'),
  path ('do_add_course/', views.do_add_course, name='do_add_course'),
]