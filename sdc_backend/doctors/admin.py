from django.contrib import admin

from .models import DoctorsPatients, Doctor
# Register your models here.

admin.site.register(DoctorsPatients)
admin.site.register(Doctor)
