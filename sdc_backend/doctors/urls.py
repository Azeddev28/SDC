from django.urls import path, re_path

from .views import (PatientListAPIView, PatientDetailsRetrieveAPIView, 
                    PatientsMealPlanListUpdateAPIView, AppointmentListAPIView,
                    PatientInsulinScheduleListUpdateAPIView,
                    PatientGlucoseLevelHistoryListAPIView,
                    SampleMealPlanListAPIView, SendMessageAPIView)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'patient-meal-plan/(?P<patient_uuid>[0-9A-Fa-f-]+)', 
               PatientsMealPlanListUpdateAPIView, 
               basename='patients-meal-plan')

router.register(r'patient-insulin-schedule/(?P<patient_uuid>[0-9A-Fa-f-]+)', 
               PatientInsulinScheduleListUpdateAPIView, 
               basename='patient-insulin-schedule')

urlpatterns = [
     path('patient-list', PatientListAPIView.as_view(), name="patient-list"),
     path('patient-details/<uuid:uuid>', PatientDetailsRetrieveAPIView.as_view(), 
          name="patient-details"),
     # path('patient-meal-plan', PatientsMealPlanListUpdateAPIView.as_view(), 
     #      name="patient-meal-plans"),
     # path('patient-insulin-schedule', PatientInsulinScheduleListUpdateAPIView.as_view(), 
     #      name="patient-insulin-schedule"),
     path('patient-glucose-history', PatientGlucoseLevelHistoryListAPIView.as_view(), 
          name='patient-glucose-history'),
     path('appointments', AppointmentListAPIView.as_view(),
           name='appointments'),
     path('sample-mealplan/<slug:sample_name>', SampleMealPlanListAPIView.as_view(), 
          name='sample-mealplan'),
    # re_path(r'^patient/(?P<slug>[\w-]+)/$', PatientDetailsRetrieveAPIView.as_view(), name='patient-details'),
     path('send-message', SendMessageAPIView.as_view(), name="send-message"),

]

urlpatterns = urlpatterns + router.urls