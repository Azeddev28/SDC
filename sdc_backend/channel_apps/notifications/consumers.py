import json
from channels.generic.websocket import WebsocketConsumer, async_to_sync
from django.contrib.auth.models import User
from channels.layers import get_channel_layer


class NotificationConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name = str(self.scope['url_route']['kwargs']['uuid'])
        self.room_group_name = self.room_name
        async_to_sync(self.channel_layer.group_add)(
        self.room_group_name, self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
        self.room_group_name,
        self.channel_name
        )

    def receive(self, text_data=None,bytes_data = None):

        text_data_json = json.loads(text_data)

        message = text_data_json['message']
        receiver = text_data_json['receiver']
        notification_type = text_data_json['notification_type']

        print(receiver)
        uuid = text_data_json['uuid']
        # Send message to room group
        channel_layer = get_channel_layer()
        group_name = str(uuid)
        async_to_sync(channel_layer.group_send)(
        group_name, {
            'receiver': receiver,
            'notification_type': notification_type, 
            "type": "broadcast_notification_message",
            "message": "Critical Condition"
            }
        )
    # broadcast Notification; Individual + community
    def broadcast_notification_message(self, event):
        message = event['message']
        receiver = event['receiver']
        notification_type = event['notification_type']
        self.send(text_data=json.dumps({ 
        'message': message,
        'notification_type': notification_type,
        'receiver': receiver
        }))
    
class EmergencyConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name = str(self.scope['url_route']['kwargs']['uuid'])
        self.room_group_name = self.room_name
        async_to_sync(self.channel_layer.group_add)(
        self.room_group_name, self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
        self.room_group_name,
        self.channel_name
        )

    # broadcast Notification; Individual + community
    def broadcast_notification_message(self, event):
        message = event['message']
        receiver = event['receiver']
        self.send(text_data=json.dumps({ 
        'message': message,
        'receiver': receiver
        }))
    