from django.db import models
from django.utils import timezone


class GeneratedPassword(models.Model):
    """Model to store generated passwords for history"""
    password = models.CharField(max_length=255)
    length = models.IntegerField()
    include_uppercase = models.BooleanField(default=True)
    include_lowercase = models.BooleanField(default=True)
    include_numbers = models.BooleanField(default=True)
    include_symbols = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Password generated at {self.created_at.strftime('%Y-%m-%d %H:%M')}"
