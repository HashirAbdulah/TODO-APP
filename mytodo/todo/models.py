from django.db import models

class Todo(models.Model):
    Priority_choices = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)
    priority = models.CharField(max_length=6, choices=Priority_choices, default='Low')
