from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Video(models.Model):
    title = models.CharField(max_length=100)
    vid_description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    latest = models.BooleanField(default=False)
    is_vid = models.BooleanField(default=True)  #check if the post is a video - default assumptiin is yes 



    def __str__(self):
        return self.title

# Genres - Church Growth, Evangelism, Soul winning, Music, Faith, Holy Spirit, Prayer, Prosperity and Finance, Healing and Health, 
# Christian living

# Language - En Español, Franch, Portuguese, 