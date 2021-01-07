from django.urls import path, re_path

from .views import MessagesListAPIView


urlpatterns = [
     path('messages/<uuid:uuid>', MessagesListAPIView.as_view(), name="chat"),
]