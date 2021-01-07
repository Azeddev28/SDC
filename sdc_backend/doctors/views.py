from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.mixins import UpdateModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated 
from rest_framework.viewsets import GenericViewSet

from patients.models import MealPlan, MedicationSchedule, GlucoseLevelHistory

from .serializers import (DoctorsPatientsSerializer, PatientDetailsSerializer, 
                          PatientMealPlanSerializer, PatientInsulinScheduleSerializer,
                          PatientGlucoseHistorySerializer, AppointmentSerializer,
                          SampleMealPlanSerializer)

from .models import DoctorsPatients, Appointments, SampleMealPlan

from sdc.models import Messages

from rest_framework.response import Response


User = get_user_model()
# Create your views here.


class AppointmentListAPIView(ListAPIView):
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        doctor = self.request.user
        return Appointments.objects.filter(doctor=doctor)


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


class PatientsMealPlanListUpdateAPIView(ListModelMixin, UpdateModelMixin
                                             ,GenericViewSet):
    serializer_class = PatientMealPlanSerializer

    def get_queryset(self):
        patient_uuid = self.kwargs['patient_uuid']
        meal_plan_list = MealPlan.objects.filter(patient__uuid=patient_uuid)
        return meal_plan_list


class PatientInsulinScheduleListUpdateAPIView(ListModelMixin, UpdateModelMixin
                                             ,GenericViewSet):
    serializer_class = PatientInsulinScheduleSerializer

    def get_queryset(self):
        patient_uuid = self.kwargs['patient_uuid']
        insulin_schedule_list = MedicationSchedule.objects.filter(patient__uuid=patient_uuid)
        return insulin_schedule_list


class PatientGlucoseLevelHistoryListAPIView(ListAPIView):
    """API which retrieves glucose level history list for a particular patient"""
    serializer_class = PatientGlucoseHistorySerializer

    def get_queryset(self):
        patient_uuid = self.request.data.get('patient_uuid')
        glucose_level_list = GlucoseLevelHistory.objects.filter(patient__uuid=patient_uuid)
        return glucose_level_list



# class MealPlanRetrieveUpdateAPIView(RetrieveUpdateAPIView):
#     """API VIEW TO RETRIEVE AND UPDATE MEAL PLAN"""
#     serializer_class = PatientGlucoseHistorySerializer

#     def get_queryset(self):
#         patient_uuid = self.request.data.get('patient_uuid')
#         glucose_level_list = GlucoseLevelHistory.objects.filter(patient__uuid=patient_uuid)
#         return glucose_level_list

class SampleMealPlanListAPIView(ListAPIView):
    serializer_class = SampleMealPlanSerializer

    def get_queryset(self):
        sample_name = self.kwargs['sample_name']
        return SampleMealPlan.objects.filter(sample_name=sample_name)
    


class SendMessageAPIView(APIView):
    def post(self, request):
        sender = self.request.user
        patient_uuid = self.request.data.get("patient_uuid")
        receiver = User.objects.get(uuid=patient_uuid)
        message = self.request.data.get("message_body")
        Messages.objects.create(sender=sender, receiver=receiver, message=message)
        return Response({
            'sender': 'doctor',
            'message': "Messages Successfully Delivered!"
        })