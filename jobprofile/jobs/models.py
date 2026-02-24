from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class  Job(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=3000)
    company_name=models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    salary = models.IntegerField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Application(models.Model):
    job=models.ForeignKey(Job,on_delete=models.CASCADE)
    applicant=models.ForeignKey(User,on_delete=models.CASCADE)
    cover_letter=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.applicant.username} applied to {self.job.title}"