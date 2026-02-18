from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=199)
    email=models.EmailField(unique=True)
    roll=models.IntegerField()
    
    def __str__(self):
        return self.name
    
