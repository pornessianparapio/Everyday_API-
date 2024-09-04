from rest_framework import generics
from .models import Resource
from .serializers import ResourceSerializer
from rest_framework.permissions import IsAuthenticated

class ResourceListCreate(generics.ListCreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [IsAuthenticated]
