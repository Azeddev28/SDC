from django.contrib.auth import get_user_model

from rest_framework import serializers

from users.models import Profile
from patients.models import MealPlan, MedicationSchedule, GlucoseLevelHistory

from .models import DoctorsPatients


User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['address']


class DoctorsPatientsSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(read_only=True, source="patient.first_name")
    last_name = serializers.CharField(read_only=True, source="patient.last_name")


    class Meta:
        model = DoctorsPatients
        # fields = ['doctor', 'patient']
        fields = ['first_name', 'last_name']


class PatientDetailsSerializer(serializers.ModelSerializer):
    user_to_profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'user_to_profile']


class PatientMealPlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = MealPlan
        fields = ['name', 'scheduled_time']


class PatientInsulinScheduleSerializer(serializers.ModelSerializer):
    med_name = serializers.CharField(source="medication.name")
    dosage = serializers.CharField(source="medication.dosage")

    class Meta:
        model = MedicationSchedule
        fields = ['med_name', 'dosage', 'scheduled_time']


class PatientGlucoseHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = GlucoseLevelHistory
        fields = ['glucose_level', 'created_at']