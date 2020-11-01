from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from django.contrib.auth import get_user_model

from.constants import UNIQUE_USERNAME_VALIDATION_ERROR
User = get_user_model()


class SignUpSerializer(serializers.ModelSerializer):
    """Serializer for creating user"""
    username = serializers.CharField(validators=[
        UniqueValidator(queryset=User.objects.all(),
        message=UNIQUE_USERNAME_VALIDATION_ERROR)],required=False)
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    user_type = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'confirm_password', 'user_type')


    def create(self, validated_data):
        """Function to create user"""
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



class UserCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating user"""

    username = serializers.CharField(validators=[
        UniqueValidator(queryset=User.objects.all(),
        message=UNIQUE_USERNAME_VALIDATION_ERROR)],required=False)
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    user_type = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'confirm_password', 'user_type')

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
