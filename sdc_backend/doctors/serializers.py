from django.contrib.auth import get_user_model

from rest_framework import serializers

from users.models import Profile
from patients.models import MealPlan, MedicationSchedule, GlucoseLevelHistory

from .models import DoctorsPatients, Appointments, SampleMealPlan



User = get_user_model()


class AppointmentSerializer(serializers.ModelSerializer):
    patient_name = serializers.SerializerMethodField("get_patient_name")
    status = serializers.CharField(source="get_status_display")
    
    def get_patient_name(self, obj):
        return "{} {}".format(obj.patient.first_name, obj.patient.last_name)

    class Meta:
        model = Appointments
        exclude = ['id', 'updated_at', 'patient', 'doctor']
        read_only_fields = ('doctor', 'patient')

    def create(self, validated_data):
        patient = self.context.get("request").user
        doctor = patient.patient_to_doctorsPatients.doctor
        time = validated_data["time"]
        date = validated_data["date"]
        return Appointments.objects.create(doctor=doctor, patient=patient,
                                        time=time, date=date)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['address']



    
class DoctorsPatientsSerializer(serializers.ModelSerializer):
    patient_name = serializers.SerializerMethodField("get_patient_name")
    phone_number = serializers.CharField(source="patient.user_to_profile.phone_no")
    uuid = serializers.CharField(source="patient.uuid")
    def get_patient_name(self, obj):
        return "{} {}".format(obj.patient.first_name, obj.patient.last_name)

    class Meta:
        model = DoctorsPatients
        # fields = ['doctor', 'patient']
        fields = ['patient_name', 'phone_number', 'uuid']


class PatientDetailsSerializer(serializers.ModelSerializer):
    user_to_profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'user_to_profile']


class PatientMealPlanSerializer(serializers.ModelSerializer):

    meal_type = serializers.CharField(source="get_meal_type_display")
    scheduled_day = serializers.CharField(source="get_scheduled_day_display")

    patient_name = serializers.SerializerMethodField("get_patient_name")

    def get_patient_name(self, obj):
        return "{} {}".format(obj.patient.first_name, obj.patient.last_name)

    class Meta:
        model = MealPlan
        exclude = ['id', 'patient', 'created_at', 'updated_at']

class PatientInsulinScheduleSerializer(serializers.ModelSerializer):
    med_name = serializers.CharField(source="medication.name")
    dosage = serializers.CharField(source="medication.dosage")

    class Meta:
        model = MedicationSchedule
        exclude = ['id', 'patient', 'created_at', 'updated_at', 'medication']


class PatientGlucoseHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = GlucoseLevelHistory
        fields = ['glucose_level', 'created_at']


class SampleMealPlanSerializer(serializers.ModelSerializer):
    meal_type = serializers.CharField(source="get_meal_type_display")
    scheduled_day = serializers.CharField(source="get_scheduled_day_display")

    class Meta:
        model = SampleMealPlan
        exclude = ['id', 'created_at', 'updated_at']