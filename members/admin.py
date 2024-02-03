from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from members.models import CustomUser, Admin
# Register your models here.
class UserModel(UserAdmin):
  pass

admin.site.register(CustomUser,UserModel)

class AdminModel(admin.ModelAdmin):
  pass

admin.site.register(Admin,AdminModel)