from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/notification/<uuid:uuid>/', consumers.NotificationConsumer.as_asgi()),
    # path('ws/emergency/<uuid:uuid>/', consumers.EmergencyConsumer.as_asgi()),

]