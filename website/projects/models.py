from django.db import models
from users.models import User

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    project_manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='managed_projects')

    def __str__(self):
        return self.name
