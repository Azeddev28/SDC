from django.db import models
from django.contrib.auth.models import AbstractUser

from sdc.models import TimeStampMixin
# Create your models here.


class User(AbstractUser, TimeStampMixin):

    class Meta:
        db_table = 'users'
        ordering = ('-created_at',)

    is_patient = models.BooleanField()
    is_doctor = models.BooleanField()
    is_caretaker = models.BooleanField()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Profile(TimeStampMixin):

    class Meta:
        db_table = 'profiles'
        ordering = ('-created_at',)

    dob = models.DateField()
    address = models.CharField(max_length=250, null=True,)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)
