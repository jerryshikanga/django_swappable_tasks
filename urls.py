from django.urls import path

from .views import TasksHandlerView

app_name = "django_swappable_tasks"

urlpatterns = [
    path('tasks/', TasksHandlerView.as_view(), name='tasks')
]
