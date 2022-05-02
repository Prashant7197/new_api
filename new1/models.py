
from django.db import models
from new1.serializers import UserSerializer
from django.contrib.auth.models import User


class News(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        ordering = ['created']

# Create your models here.
class Company(models.Model):
    title = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = 'Companies'
    def __str__(self):
        return self.title