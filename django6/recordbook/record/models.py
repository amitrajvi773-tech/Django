from django.db import models

# Create your models here.
class record(models.Model):
    name=models.CharField(max_length=199)
    email=models.EmailField(unique=True)
    roll=models.IntegerField()
    
    def __str__(self):
        return self.name
    
