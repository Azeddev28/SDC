from django.urls import path

from .views import SignUpApiView, registration

urlpatterns = [
    path('signup', SignUpApiView.as_view(), name="signup"),
    path('register', registration, name='register')
]
