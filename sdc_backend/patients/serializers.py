from rest_framework import serializers

from users.models import User

from .models import InsulinSchedule, MealPlan

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['created_at', 'updated_at']


class InsulinScheduleSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    
    class Meta:
        model = InsulinSchedule
        exclude = ['created_at', 'updated_at']

    def create(self, validated_data):
        return InsulinSchedule.objects.create(**validated_data)
    
    
class MealPlanSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    
    class Meta:
        model = MealPlan
        exclude = ['created_at', 'updated_at']

    def create(self, validated_data):
        return MealPlan.objects.create(**validated_data)
    


