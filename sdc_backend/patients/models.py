from django.db import models

from sdc.models import TimeStampMixin, Medication

from users.models import User

# Create your models here.


class PatientHistory(TimeStampMixin):

    class Meta:
        db_table = 'patient_history'
        ordering = ('-created_at',)

    
    glucose_level = models.FloatField()
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_to_pat_hist')

    def __str__(self):
        return "{} {}".format(self.patient.first_name, self.patient.last_name)


class MedicationSchedule(TimeStampMixin):

    class Meta:
        db_table = 'medication_schedule'
        ordering = ('-created_at',)

    medication = models.ForeignKey(Medication, on_delete=models.CASCADE, related_name="medication_to_med_sch")
    scheduled_time = models.DateTimeField()
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_to_med_sch')

    def __str__(self):
        return "{} {}".format(self.patient.first_name, self.patient.last_name)


class MealPlan(TimeStampMixin):

    class Meta:
        db_table = 'meal_plan'
        ordering = ('-created_at',)
    
    name = models.CharField(max_length=100)
    scheduled_time = models.DateTimeField()
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_to_meal_plan')

    def __str__(self):
        return "{} {}".format(self.patient.first_name, self.patient.last_name)
