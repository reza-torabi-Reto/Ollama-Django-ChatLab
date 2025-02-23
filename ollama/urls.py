
from django.urls import path
from .views import *

urlpatterns = [
    path('', ollama_view, name="ollama_view"),
    path('manage_models/', manage_models, name='manage_models'),    
    path('translate/', translate_view, name='translate'),

]