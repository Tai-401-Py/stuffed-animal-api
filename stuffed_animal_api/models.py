from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class StuffedAnimal(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    manufacturer = models.CharField(max_length=64)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name