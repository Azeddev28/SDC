from django.db import models

from sdc.models import TimeStampMixin

from users.models import User
# Create your models here.


class PatientHistory(TimeStampMixin):
    glucose_level = models.FloatField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)


class InsulinSchedule(TimeStampMixin):
    insuling_dosage = models.CharField(max_length=50)
    medicine = models.CharField(max_length=100)
    scheduled_time = models.DateTimeField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)
