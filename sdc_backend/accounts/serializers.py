from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate


User = get_user_model()
# User Serializer
class UserSerializer(serializers.ModelSerializer):
  user_type = serializers.SerializerMethodField('get_user_type')
  

  def get_user_type(self, obj):
    if obj.is_patient:
      return 'patient'
    elif obj.is_doctor:
      return 'doctor'
    return ''

  class Meta:
    model = User
    fields = ['username', 'uuid', 'user_type']

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
            print(validated_data)
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