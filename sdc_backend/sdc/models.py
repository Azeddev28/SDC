from django.db import models


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



class Hospital(TimeStampMixin):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=350)
    



class HospitalUsers(models.Model):

    class Meta:
        db_table = 'hospital_users'

    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name="hospital_to_hospitalusers")
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="user_to_hospitalusers")

    def __str__(self):
        return "{}  {} {}".format(self.hospital.first_name, 
                                     self.user.first_name, self.user.last_name)



class Messages(TimeStampMixin):
    class Meta:
        db_table = 'messages'
        ordering = ('-created_at',)

    message = models.TextField()
    sender = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="sender_to_messages")
    receiver = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="receiver_to_messages")
    