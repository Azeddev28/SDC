from django.contrib import admin

from .models import DoctorsPatients, Doctor, Appointments, SampleMealPlan
# Register your models here.

admin.site.register(DoctorsPatients)
admin.site.register(Doctor)
admin.site.register(Appointments)
admin.site.register(SampleMealPlan)