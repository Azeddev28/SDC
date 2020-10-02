from django.db import models

# Create your models here.


class TimeStampMixin(models.Model):

    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
 

class Medication(TimeStampMixin):
  
    class Meta:
        db_table = 'medication'
        ordering = ('-created_at',)


    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)

    def __str__(self):
        return self.name