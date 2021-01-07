import json

from channels.generic.websocket import WebsocketConsumer, async_to_sync

from django.contrib.auth.models import User

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = str(self.scope['url_route']['kwargs']['uuid'])
        self.room_group_name = self.room_name
        async_to_sync(self.channel_layer.group_add)(
        self.room_group_name, self.channel_name)
        print("CONNECT")
        self.accept()

    def disconnect(self, close_code):
        pass

    def chat_message(self, event):
        message = event['message']
        msg_sender = event['msg_sender']

        self.send(text_data=json.dumps({ 
        'message': message,
        'msg_sender': msg_sender,
        }))