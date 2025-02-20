
from django.urls import path
from .views import *

urlpatterns = [
    path('', ollama_view, name="ollama_view"),
]