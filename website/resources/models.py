from django.db import models
from projects.models import Project


class Resource(models.Model):
    RESOURCE_TYPE_CHOICES = [
        ('Material', 'Material'),
        ('Equipment', 'Equipment'),
        ('Personnel', 'Personnel')
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    type = models.CharField(choices=RESOURCE_TYPE_CHOICES, max_length=50)
    availability = models.BooleanField(default=True)
    allocation_details = models.TextField()

    def __str__(self):
        return f'{self.name} ({self.type})'
