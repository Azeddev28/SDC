from rest_framework import serializers

from sdc.models import Messages

class MessageSerializer(serializers.ModelSerializer):
    sender_uuid = serializers.CharField(source="sender.uuid")
    receiver_uuid = serializers.CharField(source="receiver.uuid")

    class Meta:
        model = Messages
        fields = ['sender_uuid', 'receiver_uuid', 'message']