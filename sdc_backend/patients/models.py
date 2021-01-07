from django.db import models

from sdc.models import TimeStampMixin, Medication

from users.models import User

from enum import Enum

# Create your models here.


class GlucoseLevelHistory(TimeStampMixin):

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
    prescribed_interval = models.CharField(max_length=25, default=None)
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_to_med_sch')

    def __str__(self):
        return "{} {}".format(self.patient.first_name, self.patient.last_name)



class MealPlan(TimeStampMixin):

    class Meta:
        db_table = 'meal_plan'
        ordering = ('-created_at',)

    class MealType(models.TextChoices):
        BREAKFAST = '1'
        LUNCH = '2'
        SNACK = '3'
        DINNER = '4'

        def __str__(self):
            return str(self.value)


    class Day(models.TextChoices):
        MONDAY = "1"
        TUESDAY = "2"
        WEDNESDAY = "3"
        THURSDAY = "4"
        FRIDAY = "5"
        SATURDAY = "6"
        SUNDAY = "7"

        def __str__(self):
            return str(self.value)


    meal_description = models.CharField(max_length=100)
    meal_type = models.CharField(choices=MealType.choices, max_length=2, default=None)
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_to_meal_plan')
    scheduled_day = models.CharField(choices=Day.choices,max_length=2, default=None)

    def __str__(self):
        return "{} {}".format(self.patient.first_name, self.patient.last_name)


class Patient(TimeStampMixin):
    weight = models.CharField(max_length=30)
    height = models.CharField(max_length=30)
    patient = models.OneToOneField("users.User", on_delete=models.CASCADE, related_name="user_to_patient")