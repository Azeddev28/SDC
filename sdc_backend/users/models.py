import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

from sdc.models import TimeStampMixin, Hospital

from .managers import CustomUserManager

from phonenumber_field.modelfields import PhoneNumberField

from django.core.validators import RegexValidator
# from enum import IntEnum

# class Gender(IntEnum):
#     Male = 1
#     Female = 2
  
#     @classmethod
#     def choices(cls):
#         return [(key.value, key.name) for key in cls]



##ADD TEXT TRANSLATIONS

class User(AbstractUser, TimeStampMixin):

    class Meta:
        db_table = 'users'
        ordering = ('-created_at',)
    
    objects = CustomUserManager()
    email = None
    USERNAME_FIELD = 'username'
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
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)






# class PatientReports(TimeStampMixin):




class Profile(models.Model):

    class Gender(models.TextChoices):
        MALE = "1"
        FEMALE = "2"

    class Meta:
        db_table = 'profiles'

    dob = models.DateField(null=True)
    address = models.CharField(max_length=250, null=True,)
    gender = models.CharField(choices=Gender.choices, max_length=2, default=Gender.MALE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_to_profile')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_no = PhoneNumberField(validators=[phone_regex])

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)


