from django.contrib import admin

from .models import MedicationSchedule, MealPlan, PatientHistory
# Register your models here.

class MedicationScheduleAdmin(admin.ModelAdmin):
    model = MedicationSchedule
    list_display = [field.name for field in MedicationSchedule._meta.get_fields()]


class MealPlanAdmin(admin.ModelAdmin):
    model = MealPlan
    list_display = [field.name for field in MealPlan._meta.get_fields()]


class PatientHistoryAdmin(admin.ModelAdmin):
    model = PatientHistory
    list_display = [field.name for field in PatientHistory._meta.get_fields()]


admin.site.register(MedicationSchedule, MedicationScheduleAdmin)
admin.site.register(MealPlan, MealPlanAdmin)
admin.site.register(PatientHistory, PatientHistoryAdmin)


