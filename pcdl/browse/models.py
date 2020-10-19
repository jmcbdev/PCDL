from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Video(models.Model):
    title = models.CharField(max_length=100)"
    video_file = models.FileField(upload_to='browse/', null=True, verbose_name="")
    description = models.TextField()
    genres = models.CharField(max_length=100)

    def __str__(self):
        return self.title