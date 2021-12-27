from django.urls import path
from .views import get_dish


urlpatterns = [
    path('<str:dish>/', get_dish)
]