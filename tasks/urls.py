from django.urls import path
from . import views

urlpatterns = [
    path("api/tasks/", views.task_list, name="task-list"),
    path("api/tasks/create/", views.create_task, name="create-task"),
]