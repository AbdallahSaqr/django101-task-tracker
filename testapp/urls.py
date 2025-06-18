from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('task-list/', views.task_list, name='task_list'),
    path('task-detail/<int:task_id>/', views.task_detail, name='task_detail'),
    path('task/<int:task_id>/delete/', views.task_delete, name='task_delete'),
    path('task-create/', views.task_create, name='task_create'),
    path('task-update/<int:task_id>/', views.task_update, name='task_update'),
]