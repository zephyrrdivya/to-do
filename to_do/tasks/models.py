from django.db import models
from datetime import datetime, timedelta
from user.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    deadline_date = models.DateTimeField(
        default=datetime.now()+timedelta(days=7))
    isCompleted = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     super(Post, self).save(*args, **kwargs)
