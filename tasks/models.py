from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    mobile = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

class Task(models.Model):
    TASK_TYPES = (
        ('URGENT', 'Urgent'),
        ('NORMAL', 'Normal'),
        ('LOW', 'Low'),
    )
    
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
    )
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    task_type = models.CharField(max_length=20, choices=TASK_TYPES, default='NORMAL')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    completed_at = models.DateTimeField(null=True, blank=True)
    assigned_users_ids = models.ManyToManyField(User, related_name='tasks')
    
    def __str__(self):
        return self.name