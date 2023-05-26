
# Create your models here.
from django.db import models

class User(models.Model):
    FullName = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Phone = models.CharField(max_length=50)
    Address = models.CharField(max_length=300)

    def __str__(self):
        return self.FullName
