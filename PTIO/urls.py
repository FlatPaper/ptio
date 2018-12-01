from django.urls import path
import PTIO.views as views

urlpatterns = [
    path('', views.index),
    path('parent/<int:parent_id>', views.parent),
    path('teacher/<int:teacher_id>', views.teacher),
    path('student/', views.student),
    path('slot/register/<int:parent_id>/<int:slot_id>/', views.register_slot, name='register'),
    path('slot/register/complete_registration', views.register_slot_post, name='complete_registration')
]