from django.urls import path
from .views import *

urlpatterns = [
    path("car/<int:pk>", CarView.as_view({"get": "retrieve"})),
]
