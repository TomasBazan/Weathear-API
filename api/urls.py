from django.urls import path
from .views import get_mock


urlpatterns = [
    path('weather/', get_mock, name='weather'),
]
