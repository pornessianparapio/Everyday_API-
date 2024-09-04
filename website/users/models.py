
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_project_manager = models.BooleanField(default=False)
    is_worker = models.BooleanField(default=False)
