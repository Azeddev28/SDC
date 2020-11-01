from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework.views import APIView

User = get_user_model()
# Create your views here.


class AlertGlucoseAbnormalityAPIView(APIView):

    def post(self, request, *args, **kwargs):
        patient_phone_number = request.data.get("patient_phone_number")
        patient_name = request.data.get("patient_name")
        glucose_level = request.data.get("glucose_level")
        context = {
            'patient_name': patient_name,
            'patient_phone_no': patient_phone_number,
            'glucose_level': glucose_level
        }        
        return Response(context)