from django.db import models
from django.contrib.auth import get_user_model

from sdc.models import TimeStampMixin

User = get_user_model()
# Create your models here.

class DoctorsPatients(TimeStampMixin):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="doctor_to_doctorsPatients")
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="patient_to_doctorsPatients")

    def __str__(self):
        return "{} {}  {} {}".format(self.doctor.first_name, self.doctor.last_name, 
                                     self.patient.first_name, self.patient.last_name)


class Doctor(TimeStampMixin):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_to_doctor')
    visiting_hours = models.CharField(max_length=20)

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)
