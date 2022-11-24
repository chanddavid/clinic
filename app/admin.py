from django.contrib import admin

from .models import User,Role

@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display= ['id','user_name','full_name','email','phone_number','specilist','district','city','ward','hashed_password','is_superuser','is_active']
    # list_display= ['id','user_name','full_name','email','phone_number','specilist','role','district','city','ward','hashed_password','is_superuser','is_active']


@admin.register(Role)
class RoleModelAdmin(admin.ModelAdmin):
    list_display= ['id','name']