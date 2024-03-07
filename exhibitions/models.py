from django.db import models

# Create your models here.
class Exhibition(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="exhibition")
    description = models.CharField(max_length=100,default="")

    def __str__(self):
        return self.name
    
class PhotosExhibition(models.Model):
    exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="exhibition_photos")

    def __str__(self):
        return f"Fotografia de {self.exhibition.name}"