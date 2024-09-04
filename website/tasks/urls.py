from django.urls import path
from .views import TaskListCreate

urlpatterns = [
    path('', TaskListCreate.as_view(), name='task-list-create'),
]
