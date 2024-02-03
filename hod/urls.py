from django.urls import path
from . import views

urlpatterns = [
  path ('home/', views.home, name='hodHome'),
  path ('add_announcement/', views.add_announcement, name='add_announcement'),
]