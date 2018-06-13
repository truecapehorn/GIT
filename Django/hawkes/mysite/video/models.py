from django.db import models
from django.utils import timezone

# Create your models here.ha


class Video(models.Model):
    title=models.CharField(max_length=200)
    descriprion=models.TextField(max_length=500)
    upload_date=models.DateTimeField(default=timezone.now)
    video_id=models.CharField(max_length=50)
    tags=models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/video/{}'.format(self.id)
