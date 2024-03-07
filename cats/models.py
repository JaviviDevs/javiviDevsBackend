from django.db import models

SexEnum = (
	("MACHO","macho"),
	("HEMBRA","hembra")
)


# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length=100)
    sex =  models.CharField(max_length=255, choices=SexEnum)
    image = models.ImageField(upload_to="cats")
    birth_place = models.CharField(max_length=100)
    birth_date =  models.DateField()
    race = models.CharField(max_length=255)
    is_adult = models.BooleanField(default=False)
    link_pedigree = models.CharField(max_length=255,default="")
    color=models.CharField(max_length=100,default="")
    code=models.CharField(max_length=255,default="")
    father_name = models.CharField(max_length=255,default="")
    mother_name = models.CharField(max_length=255,default="")
    test = models.CharField(max_length=255,default="")
    blood_group = models.CharField(max_length=100,default="")

    def __str__(self):
        return self.name
    
class PhotosCat(models.Model):
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="cats_photos")

    def __str__(self):
        return f"Fotografia de {self.cat.name}"