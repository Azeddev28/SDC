# mysite/asgi.py
import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import sdc_backend.channel_apps.notifications.routing as notifications_routing 
import sdc_backend.channel_apps.chat.routing as chat_routing
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            notifications_routing.websocket_urlpatterns + chat_routing.websocket_urlpatterns
        )
    ),
})  