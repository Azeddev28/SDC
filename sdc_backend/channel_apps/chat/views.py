from django.shortcuts import render

from django.db.models import Q

from .serializers import MessageSerializer

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from sdc.models import Messages

from rest_framework.response import Response
# Create your views here.

class MessagesListAPIView(ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        uuid = self.kwargs['uuid']
        query = Q(sender__uuid=uuid) | Q(receiver__uuid=uuid)
        return Messages.objects.filter(query)