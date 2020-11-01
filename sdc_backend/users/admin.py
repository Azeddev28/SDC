from django.contrib import admin

from .models import User, Profile
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ['id', 'uuid', 'first_name', 'last_name', 'username', 'is_superuser', 'is_staff',
                    'is_patient', 'is_doctor']

class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = [field.name for field in Profile._meta.get_fields()]


admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)