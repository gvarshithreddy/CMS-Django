from django.urls import path
from . import views

urlpatterns = [
  path('login/', views.login_user, name='login'),
  path('do_login', views.do_login, name='do_login'),
  path('logout/', views.logout_user, name='logout'),
  path('get_user_details/', views.get_user_details, name='get_user_details'),
]