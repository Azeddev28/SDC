from django.dispatch import receiver
from django.db.models.signals import post_save
from channels.generic.websocket import WebsocketConsumer, async_to_sync
from .models import Appointments
from channels.layers import get_channel_layer

@receiver(post_save, sender=Appointments)
def appointments_post_save(sender, instance, created, **kwargs):
    print("BESTTTT")
    channel_layer = get_channel_layer()
    group_name = str(instance.doctor.uuid)
    async_to_sync(channel_layer.group_send)(
    group_name, {
            'receiver': 'doctor',
            'notification_type': "info",
            "type": "broadcast_notification_message",
            "message": "{} {} {}".format("You got an appointment request from", 
                                      instance.patient.first_name, 
                                      instance.patient.last_name)
        }
    )