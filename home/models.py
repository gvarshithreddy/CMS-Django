from django.db import models
from django.utils import timezone

# Create your models here.

class Announcement(models.Model):
    title = models.CharField(max_length=100)
    new = models.BooleanField(default=True)
    body = models.TextField()
    date = models.DateTimeField()
    # def save(self, *args, **kwargs):
    #     ''' On save, update timestamps '''
    #     self.date = timezone.now()
    #     return super(Announcement, self).save(*args, **kwargs)
    def __str__(self):
        return self.title