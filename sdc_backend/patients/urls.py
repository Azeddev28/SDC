from django.urls import path, include

from .views import MedicationScheduleListCreateAPIView

urlpatterns = [
    path('insulin-schedule', MedicationScheduleListCreateAPIView.as_view(), name="insulin-schedule"),
]
