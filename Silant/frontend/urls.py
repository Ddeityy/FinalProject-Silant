from django.urls import path
from .views import index

urlpatterns = [
    path("", index),
    path("car/", index),
    path("info/", index),
]
