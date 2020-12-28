from django.db import models
from django.utils import timezone

class Video(models.Model):
    videotitle = models.CharField(max_length=30)
    videodesc = models.TextField()
    date_added  = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'name: {},ID: {}'.format(self.videotitle, self.id)
