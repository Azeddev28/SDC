from django.shortcuts import render
from django.utils.decorators import method_decorator

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView

from sdc.decorators import log_api

from .constants import PROFILE_UPDATION_ERROR, USER_NOT_CREATED_ERROR
from .serializers import SignUpSerializer

from django.contrib.auth import get_user_model


from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework import response, decorators, permissions, status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserCreateSerializer


User = get_user_model()
# Create your views here.


# @method_decorator(log_api(error_msg=PROFILE_UPDATION_ERROR), name='post')
class ProfileUpdateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        return Response({
            'success_message': "Profile Updated Successfully"
        })

#LOGIN API
# class LoginAPIView(self, request, *args, **kwargs):

#SIGNUP API
# @method_decorator(log_api(USER_NOT_CREATED_ERROR),name='create')
class SignUpApiView(CreateAPIView):
    """Handle user creation"""
    serializer_class = SignUpSerializer



@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def registration(request):
    serializer = UserCreateSerializer(data=request.data)
    if not serializer.is_valid():
        return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)        
    user = serializer.save()
    refresh = RefreshToken.for_user(user)
    res = {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }
    return response.Response(res, status.HTTP_201_CREATED)