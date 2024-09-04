from django.urls import path
from .views import ResourceListCreate

urlpatterns = [
    path('', ResourceListCreate.as_view(), name='resource-list-create'),
]
