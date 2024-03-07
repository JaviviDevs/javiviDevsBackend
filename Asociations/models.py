from django.db import models

# Create your models here.
class Asociation(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="asociations")

    def __str__(self):
        return self.title
      