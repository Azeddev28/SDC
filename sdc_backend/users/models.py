from django.db import models
from django.contrib.auth.models import AbstractUser

from sdc.models import TimeStampMixin
# Create your models here.

##ADD TEXT TRANSLATIONS

class User(AbstractUser, TimeStampMixin):

    class Meta:
        db_table = 'users'
        ordering = ('-created_at',)

    email = None
    REQUIRED_FIELDS = []
    is_patient = models.BooleanField(
        default=False,
        help_text=(
            'If this flag is true it means user is a patient.'
        ),
    )
    is_doctor = models.BooleanField(
        default=False,
        help_text=(
            'If this flag is true it means user is a doctor.'
        ),
    )
    is_caretaker = models.BooleanField(
        default=False,
        help_text=(
            'If this flag is true it means user is a care taker.'
        ),
    )

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Doctor(TimeStampMixin):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_to_doctor')
    visiting_hours = models.CharField(max_length=20)

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)


class Profile(TimeStampMixin):

    class Meta:
        db_table = 'profiles'
        ordering = ('-created_at',)

    dob = models.DateField()
    address = models.CharField(max_length=250, null=True,)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_to_profile')
    
    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)
