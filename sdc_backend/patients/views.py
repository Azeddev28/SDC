from django.utils.decorators import method_decorator
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 

from sdc_backend.sdc.decorators import log_api

from .models import MedicationSchedule, MealPlan, GlucoseLevelHistory
from .constants import (GLUCOSE_CHECK_ERROR, GLUCOSE_PREDICTION_ERROR, MEAL_PLAN_ERROR, 
                        LIST_DISPLAY_ERROR)
from .utils import fetch_glucose_level, predict_glucose_reading
from .serializers import MedicationScheduleSerializer, MealPlanSerializer, GlucoseLevelSerializer


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
