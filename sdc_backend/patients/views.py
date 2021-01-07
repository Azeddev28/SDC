from django.utils.decorators import method_decorator
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated 

from sdc_backend.sdc.decorators import log_api
from sdc.models import Messages

from .renderers import JPEGRenderer, PNGRenderer

from doctors.models import Appointments
from doctors.serializers import AppointmentSerializer

from .models import MedicationSchedule, MealPlan, GlucoseLevelHistory
from .constants import (GLUCOSE_CHECK_ERROR, GLUCOSE_PREDICTION_ERROR, MEAL_PLAN_ERROR, 
                        LIST_DISPLAY_ERROR)
from .utils import fetch_glucose_level, predict_glucose_reading
from .serializers import (MedicationScheduleSerializer, MealPlanSerializer, 
                          GlucoseLevelSerializer, PatientSerializer)

from django.contrib.auth import get_user_model

import datetime

from .gangerene_detection_helpers import detect_gangerene

from wsgiref.util import FileWrapper
from django.http.response import HttpResponse

User = get_user_model()

class AppointmentCreateAPIView(CreateAPIView):
    serializer_class = AppointmentSerializer


# @method_decorator(log_api(error_msg=GLUCOSE_CHECK_ERROR), name='post')
class GlucoseLevelListCreateAPIView(ListCreateAPIView):
    serializer_class = GlucoseLevelSerializer

    def get_queryset(self):
        return GlucoseLevelHistory.objects.filter(patient=self.request.user)
    


# @method_decorator(log_api(error_msg=GLUCOSE_PREDICTION_ERROR), name='post')
class PredictGlucoseLevelAPIView(APIView):
    def post(self, request, *args, **kwargs):
        predicted_glucose_level = predict_glucose_reading()
        return Response({
            'predicted_glucose_level': predicted_glucose_level
        })


# @method_decorator(log_api(error_msg=GLUCOSE_PREDICTION_ERROR), name='post')
class MedicationScheduleViewset(ModelViewSet):
    permission_classes = [IsAuthenticated,]
    serializer_class = MedicationScheduleSerializer
    http_method_names = ['get', 'post', 'head', 'put']

    def get_queryset(self):
        user_id = self.request.user.id
        insulin_schedule_list = MedicationSchedule.objects.filter(patient_id=user_id)
        return insulin_schedule_list
    
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


# @method_decorator(log_api(error_msg=LIST_DISPLAY_ERROR), name='list')
class MealPlanViewset(ModelViewSet):
    serializer_class = MealPlanSerializer
    http_method_names = ['get', 'post', 'head', 'put']
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        user_id = self.request.user.id
        meal_plan_list = MealPlan.objects.filter(patient_id=user_id)
        return meal_plan_list
    
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)



class GetLastAppointmentAPIView(APIView):
        
    def get(self, request, *args, **kwargs):
        appointment = Appointments.objects.filter(patient=self.request.user)\
                      .first()
        return Response({
            'last_appointment_date': appointment.date.strftime("%b,%m %y")
        })



class GetAssociatedDoctorAPIView(APIView):
    def get(self, request):
        doctor = request.user.patient_to_doctorsPatients.doctor
        return Response({
            'doctor_name': "{} {}".format(doctor.first_name, doctor.last_name),
            'doctor_phone_no': str(doctor.user_to_profile.phone_no),
            'patient_uuid': request.user.uuid
        })


class SendMessageAPIView(APIView):
    def post(self, request):
        sender = self.request.user
        receiver = request.user.patient_to_doctorsPatients.doctor
        message = self.request.data.get("message_body")
        Messages.objects.create(sender=sender, receiver=receiver, message=message)
        return Response({
            'sender': 'patient',
            'message': "Messages Successfully Delivered!"
        })





from PIL import Image 

def to_image(numpy_img):
    img = Image.fromarray(numpy_img, 'RGB')
    return img


import base64
from io import BytesIO

def to_data_uri(pil_img):
    data = BytesIO()
    pil_img.save(data, "JPEG") # pick your format
    data64 = base64.b64encode(data.getvalue())
    return u'data:img/jpeg;base64,'+data64.decode('utf-8') 

class GangereneDetectionAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser, )
    renderer_classes = [JPEGRenderer, PNGRenderer]

    def post(self, request, *args, **kwargs):
        picture = request.data['image']
        # picture
        # Use your model to handle the uploaded file
        image = detect_gangerene(picture)
        im = to_image(image)
        to_data_uri(im)
        return Response(im, content_type="image/jpeg")