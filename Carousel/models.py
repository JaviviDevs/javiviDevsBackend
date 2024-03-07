from django.db import models

# Create your models here.
class CarouselElement(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100,default=(""))
    image = models.ImageField(upload_to="carousel")

    def __str__(self):
        return self.title
