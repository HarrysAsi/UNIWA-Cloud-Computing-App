from django.urls import path
from .views import (
    subject_exercises_view
)

urlpatterns = [
    path('<int:pk>/', subject_exercises_view, name='subject'),
]
