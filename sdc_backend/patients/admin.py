from django.contrib import admin

from .models import MedicationSchedule, MealPlan, GlucoseLevelHistory, Patient
# Register your models here.

class MedicationScheduleAdmin(admin.ModelAdmin):
    model = MedicationSchedule
    list_display = [field.name for field in MedicationSchedule._meta.get_fields()]


class MealPlanAdmin(admin.ModelAdmin):
    model = MealPlan
    list_display = [field.name for field in MealPlan._meta.get_fields()]


class GlucoseLevelHistoryAdmin(admin.ModelAdmin):
    model = GlucoseLevelHistory
    list_display = [field.name for field in GlucoseLevelHistory._meta.get_fields()]


admin.site.register(MedicationSchedule, MedicationScheduleAdmin)
admin.site.register(MealPlan, MealPlanAdmin)
admin.site.register(GlucoseLevelHistory, GlucoseLevelHistoryAdmin)
admin.site.register(Patient)


