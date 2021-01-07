from django.db import models
from django.contrib.auth import get_user_model

from sdc.models import TimeStampMixin

User = get_user_model()
# Create your models here.

class DoctorsPatients(TimeStampMixin):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="doctor_to_doctorsPatients")
    patient = models.OneToOneField(User, on_delete=models.CASCADE, related_name="patient_to_doctorsPatients")

    def __str__(self):
        return "{} {}  {} {}".format(self.doctor.first_name, self.doctor.last_name, 
                                     self.patient.first_name, self.patient.last_name)


class Doctor(TimeStampMixin):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_to_doctor')
    visiting_hours = models.CharField(max_length=20)

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)


class Appointments(TimeStampMixin):
    class Status(models.TextChoices):
        APPROVED = '1'
        DECLINED = '2'
        PENDING = '3'


    doctor = models.ForeignKey(User, on_delete=models.CASCADE, 
                              related_name="doctor_to_appointment")
    patient = models.ForeignKey(User, on_delete=models.CASCADE, 
                                related_name="patient_to_appointment")
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(choices=Status.choices, max_length=2, default=Status.PENDING)


class SampleMealPlan(TimeStampMixin):
    sample_name = models.CharField(max_length=30)

    class MealType(models.TextChoices):
        BREAKFAST = '1'
        LUNCH = '2'
        SNACK = '3'
        DINNER = '4'

    class Day(models.TextChoices):
        MONDAY = "1"
        TUESDAY = "2"
        WEDNESDAY = "3"
        THURSDAY = "4"
        FRIDAY = "5"
        SATURDAY = "6"
        SUNDAY = "7"


    meal_description = models.CharField(max_length=100)
    meal_type = models.CharField(choices=MealType.choices, max_length=2, default=None)
    scheduled_day = models.CharField(choices=Day.choices,max_length=2, default=None)

    def __str__(self):
        return self.sample_name
