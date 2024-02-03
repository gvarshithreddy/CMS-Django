from django.urls import path
from . import views

urlpatterns = [
  path ('home/', views.studentHome, name='studentHome'),
  # path ('add_staff/', views.add_staff, name='add_staff'),
]