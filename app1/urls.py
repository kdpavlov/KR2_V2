from django.urls import path
from .views import study_records

urlpatterns = [
    path('', study_records, name='study_records'),
]