from django.urls import path
from . import views

urlpatterns = [
  path ('', views.home, name='home'),
  path ('announcements/', views.announcements, name='announcements'),
  path ('add_announcement/', views.add_announcement, name='add_announcement'),
]