from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class User(AbstractUser, TimeStampMixin):
    is_patient = models.BooleanField()
    is_doctor = models.BooleanField()
    is_caretaker = models.BooleanField()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class PatientHistory(TimeStampMixin):
    glucose_level = models.FloatField()


class Profile(models.Model):
    dob = models.DateField()
    address = models.CharField(max_length=250, null=True,)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

    