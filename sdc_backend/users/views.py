from django.shortcuts import render
from django.utils.decorators import method_decorator

from rest_framework import APIView
from rest_framework.response import Response

from sdc.decorators import log_api

from .constants import PROFILE_UPDATION_ERROR
# Create your views here.


@method_decorator(log_api(error_msg=PROFILE_UPDATION_ERROR), name='post')
class ProfileUpdateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        return Response({
            'success_message': "Profile Updated Successfully"
        })

#LOGIN API
# class LoginAPIView(self, request, *args, **kwargs):

#SIGNUP API
# class SignupAPIView(self, request, *args, **kwargs):