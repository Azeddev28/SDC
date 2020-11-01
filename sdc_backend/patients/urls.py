from django.urls import path

from .views import MedicationScheduleViewset, MealPlanViewset, GlucoseLevelListCreateAPIView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'meal-plan', MealPlanViewset, basename='meal-plan')
router.register(r'medication-schedule', MedicationScheduleViewset, basename='medication-schedule')

urlpatterns = [
    path('check-glucose-level', GlucoseLevelListCreateAPIView.as_view(), name='check-glucose-level')
    # path('medication-schedule', MedicationScheduleListCreateAPIView.as_view(), name="medication-schedule"),
]

urlpatterns = urlpatterns + router.urls
