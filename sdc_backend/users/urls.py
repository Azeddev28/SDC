from django.urls import path

from .views import SignUpApiView, registration, GetUserAPIView

urlpatterns = [
    path('signup', SignUpApiView.as_view(), name="signup"),
    path('register', registration, name='register'),
    path('get-user/<uuid:uuid>', GetUserAPIView.as_view(), name='get-user')

]
