from django.urls import path
from . import views

urlpatterns = [
    path('page/<int:id>/', views.page_detail, name='page_detail'),
    path('students/', views.students_list, name='students_list'),
]