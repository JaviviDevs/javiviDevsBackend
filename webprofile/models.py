from django.db import models

# Create your models here.
class WebProfile(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="webprofile")

    def __str__(self):
        return self.title