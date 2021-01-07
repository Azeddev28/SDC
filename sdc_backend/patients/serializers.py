from rest_framework import serializers

from django.contrib.auth import  get_user_model

from .models import MedicationSchedule, MealPlan, GlucoseLevelHistory
from .utils import fetch_glucose_level


User = get_user_model()

class PatientSerializer(serializers.ModelSerializer):
    """Serializer for serializing patient data"""
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']


class MedicationScheduleSerializer(serializers.ModelSerializer):
    """Serializer for serializing medication schedule for a particular patient"""
    # patient = PatientSerializer(many=False)
    medication = serializers.CharField(read_only=True, source="medication.name")
    class Meta:
        model = MedicationSchedule
        exclude = ['id', 'patient', 'created_at', 'updated_at']

    def create(self, validated_data):
        return MedicationSchedule.objects.create(**validated_data)
    
    
class MealPlanSerializer(serializers.ModelSerializer):
    """Serializer for serializing meal plan for a particular patient"""
    meal_type = serializers.CharField(source="get_meal_type_display")
    scheduled_day = serializers.CharField(source="get_scheduled_day_display")

    class Meta:
        model = MealPlan
        exclude = ['created_at', 'updated_at', 'patient', 'id']

    def create(self, validated_data):
        return MealPlan.objects.create(**validated_data)
    

class GlucoseLevelSerializer(serializers.ModelSerializer):
    """Serializer to create glucose level history for a patient"""

    class Meta:
        model = GlucoseLevelHistory
        fields = ['glucose_level', 'created_at']
        read_only_fields = ['created_at']

    def create(self, validated_data):
        glucose_level = validated_data.pop("glucose_level")
        print(glucose_level)
        print(glucose_level)
        print(glucose_level)

        patient = self.context.get("request").user
        return GlucoseLevelHistory.objects.create(glucose_level=glucose_level, 
                                                  patient=patient)