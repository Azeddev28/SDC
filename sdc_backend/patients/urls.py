from django.urls import path

from .views import (MedicationScheduleViewset, MealPlanViewset, 
                   GlucoseLevelListCreateAPIView, AppointmentCreateAPIView,
                   GetLastAppointmentAPIView, GetAssociatedDoctorAPIView,
                   SendMessageAPIView, GangereneDetectionAPIView)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'meal-plan', MealPlanViewset, basename='meal-plan')
router.register(r'insulin-schedule', MedicationScheduleViewset, basename='insulin-schedule')

urlpatterns = [
    path('glucose-level', GlucoseLevelListCreateAPIView.as_view(), name='glucose-level'),
    path('request-appointment', AppointmentCreateAPIView.as_view(), name='create-appointent'),
    path('last-appointment', GetLastAppointmentAPIView.as_view(), name="last-appointment"),
    path('patient-doctor', GetAssociatedDoctorAPIView.as_view(), name="patient-doctor"),
    path('send-message', SendMessageAPIView.as_view(), name="send-message"),
    path('gangerene-detection', GangereneDetectionAPIView.as_view(), 
         name="gangerene-detection")
]

urlpatterns = urlpatterns + router.urls
