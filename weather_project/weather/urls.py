from django.urls import path
from .views import get_weather_forecast

urlpatterns = [
    path('weather/', get_weather_forecast, name='weather-forecast'),
]
