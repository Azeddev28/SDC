from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import (UserSerializer, PatientLoginSerializer ,RegisterSerializer, 
                         LoginSerializer, DoctorLoginSerializer)
from rest_framework import status

# Register API
class RegisterAPI(generics.GenericAPIView):
  serializer_class = RegisterSerializer
  permission_classes = []

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    return Response({
      "user": UserSerializer(user, context=self.get_serializer_context()).data,
      "token": AuthToken.objects.create(user)[1]
    })

# Login API
class LoginAPI(generics.GenericAPIView):
  serializer_class = LoginSerializer
  permission_classes = []


  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data 
    token = AuthToken.objects.create(user)[1]
    user_data = None
    context = {}
    if user.is_patient:
      user_data = PatientLoginSerializer(user, context=self.get_serializer_context()).data

    elif user.is_doctor:
      user_data = DoctorLoginSerializer(user, context=self.get_serializer_context()).data

    else:
      user_data = UserSerializer(user, context=self.get_serializer_context()).data
   
    context.update({
      "user": user_data,
      "token": token,
      "message": "User Logged In Successfully!"
    })
    return Response(context, status=status.HTTP_200_OK)

# Get User API
class UserAPI(generics.RetrieveAPIView):
  permission_classes = [
    permissions.IsAuthenticated,
  ]
  serializer_class = UserSerializer

  def get_object(self):
    return self.request.user