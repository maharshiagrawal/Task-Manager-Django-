# TaskManager/urls.py

from django.contrib import admin
from django.urls import path
from tasks import views  # Import views from the tasks app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.task_list, name='task_list'),  # Task list page
    path('create/', views.task_create, name='task_create'),  # Task creation page
    path('<int:pk>/update/', views.task_update, name='task_update'),  # Update a task
    path('<int:pk>/delete/', views.task_delete, name='task_delete'),  # Delete a task
]
