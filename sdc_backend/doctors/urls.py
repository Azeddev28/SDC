from django.urls import path, re_path

from .views import (PatientListAPIView, PatientDetailsRetrieveAPIView, 
                    PatientsMealPlanListAPIView, PatientInsulinScheduleListAPIView,
                    PatientGlucoseLevelHistoryListAPIView)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register(r'patients', PatientListAPIView, basename='patients')

urlpatterns = [
    path('patient-list', PatientListAPIView.as_view(), name="patient-list"),
    path('patient/<uuid:uuid>', PatientDetailsRetrieveAPIView.as_view(), name="patient-details"),
    path('patient-meal-plans', PatientsMealPlanListAPIView.as_view(), name="patient-meal-plans"),
    path('patient-insulin-schedule', PatientInsulinScheduleListAPIView.as_view(), 
         name="patient-insulin-schedule"),
    path('patient-glucose-history', PatientGlucoseLevelHistoryListAPIView.as_view(), 
         name='patient-glucose-history')
    # re_path(r'^patient/(?P<slug>[\w-]+)/$', PatientDetailsRetrieveAPIView.as_view(), name='patient-details'),
]

urlpatterns = urlpatterns