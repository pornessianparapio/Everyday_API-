from django.urls import path
from .views import ProjectListCreate

urlpatterns = [
    path('', ProjectListCreate.as_view(), name='project-list-create'),
]
