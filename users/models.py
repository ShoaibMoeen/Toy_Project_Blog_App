from django.db import models
from django.contrib.auth.models import AbstractUser
from article.models import Article
from datetime import datetime, timedelta


class Writer(AbstractUser):
    is_editor = models.BooleanField(default=False)
    name = models.CharField(max_length=255)

    @property
    def total_articles(self):
        return Article.objects.filter(written_by=self.id, status="Approved").count()

    @property
    def recent_articles(self):
        prev_date = datetime.now() - timedelta(days=30)
        return Article.objects.filter(
            written_by=self.id, status="Approved", created_at__gte=prev_date
        ).count()
