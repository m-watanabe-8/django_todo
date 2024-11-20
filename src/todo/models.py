import uuid
from django.db import models

class TodoModel(models.Model):
    STATUS_CHOICES = [
        ('not_started', '未着手'),
        ('start', '着手'),
        ('completed', '完了'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default='not_started'
    )

    def __str__(self):
        return self.title