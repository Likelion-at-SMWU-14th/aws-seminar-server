from django.urls import path
from .views import home, health_check, api_test

urlpatterns = [
    path("", home),
    path("health/", health_check),
    path("api/", api_test),
]