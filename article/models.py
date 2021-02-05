from django.db import models
from datetime import datetime


# Create your models here.


class Article(models.Model):
    created_at = models.DateTimeField(default=datetime.now)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=8000)
    status = models.CharField(max_length=255, default="pending")
    written_by = models.ForeignKey(
        "users.Writer", models.SET_NULL, null=True, related_name="Writer"
    )

    edited_by = models.ForeignKey(
        "users.Writer", models.SET_NULL, null=True, related_name="Editor"
    )

    def __str__(self):
        return self.title
