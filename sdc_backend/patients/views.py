from django.utils.decorators import method_decorator
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from sdc_backend.sdc.decorators import log_api

from .models import MedicationSchedule, MealPlan
from .constants import GLUCOSE_CHECK_ERROR, GLUCOSE_PREDICTION_ERROR, PROFILE_UPDATION_ERROR 
from .utils import fetch_glucose_level, predict_glucose_reading
from .serializers import MedicationScheduleSerializer
# Create your views here.


@method_decorator(log_api(error_msg=GLUCOSE_CHECK_ERROR), name='post')
class CheckGlucoseLevelAPIView(APIView):
    def post(self, request, *args, **kwargs):
        glucose_level = fetch_glucose_level()
        return Response({
            'glucose_level': glucose_level
        })


@method_decorator(log_api(error_msg=GLUCOSE_PREDICTION_ERROR), name='post')
class PredictGlucoseLevelAPIView(APIView):
    def post(self, request, *args, **kwargs):
        predicted_glucose_level = predict_glucose_reading()
        return Response({
            'predicted_glucose_level': predicted_glucose_level
        })

@method_decorator(log_api(error_msg=GLUCOSE_PREDICTION_ERROR), name='post')
class MedicationScheduleListCreateAPIView(ListCreateAPIView):
    serializer_class = MedicationScheduleSerializer
    
    def get_queryset(self):
        user_id = self.request.user.id
        insulin_schedule_list = MedicationSchedule.objects.filter(user_id=user_id)
        return insulin_schedule_list
    
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class MealPlanListAPIView(ListCreateAPIView):
    serializer_class = MealPlanSerializer
    
    def get_queryset(self):
        user_id = self.request.user.id
        insulin_schedule_list = MedicationSchedule.objects.filter(user_id=user_id)
        return insulin_schedule_list
    
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
