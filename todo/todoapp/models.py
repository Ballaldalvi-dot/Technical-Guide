from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Todo(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
    title=models.CharField(max_length=300)
    description=models.TextField()
    completed=models.BooleanField(default=False)
    reminder = models.DateTimeField(null=True, blank=True)
    assigned_to = models.CharField(max_length=100, blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    notified = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=100, related_name='todos')  # Link to the User model
    shared_with = models.ManyToManyField(User, related_name='shared_tasks', blank=True)


