from django.dispatch import receiver
from django.db.models.signals import post_save
from channels.generic.websocket import WebsocketConsumer, async_to_sync
from channels.layers import get_channel_layer
from .models import Messages

@receiver(post_save, sender=Messages)
def message_post_save(sender, instance, created, **kwargs):
    print("guess")
    print("BaSTTTTitaaa")

    channel_layer = get_channel_layer()
    msg_sender = None
    group_name = None
    if instance.receiver.is_doctor:
        msg_sender = "patient"
        group_name = str(instance.receiver.uuid)

    else:
        msg_sender = "doctor"
        group_name = str(instance.sender.uuid)

    async_to_sync(channel_layer.group_send)(
        group_name, {
                "type": "chat_message",
                "message": instance.message,
                "msg_sender": msg_sender,
            }
    )