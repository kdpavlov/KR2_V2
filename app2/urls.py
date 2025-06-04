from django.urls import path
from . import views

urlpatterns = [
    path('page/<int:id>/', views.page_detail, name='page_detail'),
    path('students/', views.students_list, name='students_list'),
    path('management_page/', views.management_view, name='management'),
    path('my_page/', views.my_page, name='mypage'),
    path('program/', views.program_page, name='program')
]