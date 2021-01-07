from rest_framework import serializers

from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

from doctors.models import DoctorsPatients

from datetime import date

User = get_user_model()

class PatientDoctorSerializer(serializers.ModelSerializer):
  uuid = serializers.CharField(source="doctor.uuid")
  name = serializers.SerializerMethodField("get_doctor_name")
  
  def get_doctor_name(self, obj):
      return "{} {}".format(obj.doctor.first_name, obj.doctor.last_name)


  class Meta:
    model = DoctorsPatients
    fields = ['name', 'uuid']
    

# User Serializer
class PatientLoginSerializer(serializers.ModelSerializer):
  user_type = serializers.ReadOnlyField(default="patient")
  doctor = PatientDoctorSerializer(source="patient_to_doctorsPatients")  
  name = serializers.SerializerMethodField("get_patient_name")

  def get_patient_name(self, obj):
      return "{} {}".format(obj.first_name, obj.last_name)

  class Meta:
    model = User
    fields = ['username', 'uuid', 'user_type', 'name',
              'doctor']

class DoctorLoginSerializer(serializers.ModelSerializer):
  user_type = serializers.ReadOnlyField(default="doctor")

  class Meta:
    model = User
    fields = ['username', 'uuid', 'user_type', 'first_name', 'last_name']



class UserSerializer(serializers.ModelSerializer):
  user_type = serializers.SerializerMethodField('get_user_type')
  address = serializers.CharField(source="user_to_profile.address")  
  height = serializers.CharField(source="user_to_patient.height")
  weight = serializers.CharField(source="user_to_patient.weight")
  age = serializers.SerializerMethodField('get_user_age')
  doctor = serializers.SerializerMethodField('get_doctor_name')

  def get_doctor_name(self, obj):
    return "{} {}".format(obj.patient_to_doctorsPatients.doctor.first_name, 
                          obj.patient_to_doctorsPatients.doctor.last_name)

  def get_user_age(self, obj):
    dob = obj.user_to_profile.dob.strftime('%y')
    date_today = date.today().strftime('%y')
    age = int(date_today) - int(dob)
    return str(age)


  def get_user_type(self, obj):
    if obj.is_patient:
      return 'patient'
    elif obj.is_doctor:
      return 'doctor'
    return ''

  class Meta:
    model = User
    fields = ['username', 'uuid', 'user_type', 'first_name', 'last_name',
              'address', 'height', 'weight', 'age', 'doctor']

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    user_type = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
   
    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password', 'user_type']
        extra_kwargs = {'password': {'write_only': True}}
    

    def create(self, validated_data):
        if validated_data['password'] == validated_data['confirm_password']:
            user_dict = {}
            user_type = validated_data.pop("user_type")
            user_type = '{}_{}'.format("is",user_type)
            user_dict[user_type] = True
            for field in self.fields:
                if not field in ['passowrd', 'confirm_password', 'user_type']:
                    user_dict[field] = validated_data[field]
            
            user = User.objects.create(**user_dict)
            user.set_password(validated_data['password'])
            user.save()
            return user
        else:
            raise Exception('Password and confirm_password does not match')


# Login Serializer
class LoginSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField()

  def validate(self, data):
    user = authenticate(**data)
    if user and user.is_active:
      return user
    raise serializers.ValidationError("Incorrect Credentials")