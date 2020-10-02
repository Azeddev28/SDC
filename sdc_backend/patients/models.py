from django.db import models

from sdc.models import TimeStampMixin, Medication

from users.models import User

# Create your models here.


class PatientHistory(TimeStampMixin):

    class Meta:
        db_table = 'patient_history'
        ordering = ('-created_at',)

    
    glucose_level = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)


class InsulinSchedule(TimeStampMixin):

    class Meta:
        db_table = 'insulin_schedule'
        ordering = ('-created_at',)

    insuling_dosage = models.CharField(max_length=50)
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    scheduled_time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)


class MealPlan(TimeStampMixin):

    class Meta:
        db_table = 'meal_plan'
        ordering = ('-created_at',)
    
    name = models.CharField(max_length=100)
    scheduled_time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)
