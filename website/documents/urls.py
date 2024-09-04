from django.urls import path
from .views import DocumentListCreate

urlpatterns = [
    path('', DocumentListCreate.as_view(), name='document-list-create'),
]
