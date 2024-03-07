# Create your models here.

from django.db import models

# Create your models here.
class ContactCard(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    image = models.ImageField(upload_to="contactCard")

    def __str__(self):
        return self.title