from django.db import models
from django.utils import timezone

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    priority = models.CharField(choices=[('High','High'),('Medium','Medium'),('Low','Low')],max_length=10)

    def __str__(self):
        return self.title
