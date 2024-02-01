from django.urls import path
from . import views

urlpatterns = [
  path ('home/', views.studentHome, name='studentHome'),
  # path ('logout/', views.logout_user, name='logout'),
]