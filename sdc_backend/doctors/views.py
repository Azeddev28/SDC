from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated 

from patients.models import MealPlan, MedicationSchedule, GlucoseLevelHistory

from .serializers import (DoctorsPatientsSerializer, PatientDetailsSerializer, 
                          PatientMealPlanSerializer, PatientInsulinScheduleSerializer,
                          PatientGlucoseHistorySerializer)
from .models import DoctorsPatients


User = get_user_model()
# Create your views here.


class PatientListAPIView(ListAPIView):
    serializer_class = DoctorsPatientsSerializer
 
    def get_queryset(self):
        doctor = self.request.user
        patient_list = DoctorsPatients.objects.filter(doctor=doctor)
        return patient_list


class PatientDetailsRetrieveAPIView(RetrieveAPIView):
    serializer_class = PatientDetailsSerializer
    lookup_field = "uuid"
    queryset = User.objects.all()


class PatientsMealPlanListAPIView(ListAPIView):
    serializer_class = PatientMealPlanSerializer
    
    def get_queryset(self):
        patient_uuid = self.request.data.get('patient_uuid')
        meal_plan_list = MealPlan.objects.filter(patient__uuid=patient_uuid)
        return meal_plan_list


class PatientInsulinScheduleListAPIView(ListAPIView):
    serializer_class = PatientInsulinScheduleSerializer
    
    def get_queryset(self):
        patient_uuid = self.request.data.get('patient_uuid')
        insulin_schedule_list = MedicationSchedule.objects.filter(patient__uuid=patient_uuid)
        return insulin_schedule_list


class PatientGlucoseLevelHistoryListAPIView(ListAPIView):
    """API which retrieves glucose level history list for a particular patient"""
    serializer_class = PatientGlucoseHistorySerializer

    def get_queryset(self):
        patient_uuid = self.request.data.get('patient_uuid')
        glucose_level_list = GlucoseLevelHistory.objects.filter(patient__uuid=patient_uuid)
        return glucose_level_list