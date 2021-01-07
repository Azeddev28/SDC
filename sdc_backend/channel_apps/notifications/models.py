from django.db import models
from sdc_backend.sdc.models import TimeStampMixin
# Create your models here.

class Notification(TimeStampMixin):
    notification_type = models.CharField(max_length=30)
    sender_name = models.CharField(max_length=20)
    receiver_name = models.CharField(max_length=20)

