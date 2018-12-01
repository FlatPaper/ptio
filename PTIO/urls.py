from django.urls import path
import PTIO.views as views

urlpatterns = [
    path('', views.index),
    path('parent/<int:parent_id>', views.parent),
    path('teacher/<int:teacher_id>', views.teacher),
    path('student/', views.student)
]