from django.utils.decorators import method_decorator
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .decorators import log_api
from .constants import GLUCOSE_CHECK_ERROR
from .utils import fetch_glucose_level, predict_glucose_reading
# Create your views here.


@method_decorator(log_api(error_msg=GLUCOSE_CHECK_ERROR), name='post')
class CheckGlucoseLevelAPIView(APIView):
    def post(self, request, *args, **kwargs):
        glucose_level = fetch_glucose_level()
        return Response({
            'glucose_level': glucose_level
        })


@method_decorator(log_api(error_msg=GLUCOSE_CHECK_ERROR), name='post')
class PredictGlucoseLevelAPIView(APIView):
    def post(self, request, *args, **kwargs):
        predicted_glucose_level = predict_glucose_reading()
        return Response({
            'predicted_glucose_level': predicted_glucose_level
        })