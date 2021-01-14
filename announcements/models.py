from django.db import models
from django.urls import reverse

# Create your models here.

class Announcements(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('announcements:single', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['created_at']