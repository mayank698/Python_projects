from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Password(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='passwords')
    website = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.website} - {self.username}"
    
    class Meta:
        unique_together = ('user', 'website')
        verbose_name = 'Password'
        verbose_name_plural = 'Passwords'
