from django.db import models
from django.contrib.auth.models import User

class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    powers = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name