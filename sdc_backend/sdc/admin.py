from django.contrib import admin

from .models import Medication
# Register your models here.


class MedicationAdmin(admin.ModelAdmin):
    model = Medication
    list_display = ['id', 'name', 'dosage', 'created_at', 'updated_at']


admin.site.register(Medication, MedicationAdmin)