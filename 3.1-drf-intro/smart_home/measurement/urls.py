from django.urls import path
from .views import SensorView, SensorUpdateView, MeasuremetView

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', SensorUpdateView.as_view()),
    path('measurements/', MeasuremetView.as_view()),
]
