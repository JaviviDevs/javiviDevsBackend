from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):				 
    email = models.EmailField(unique=True)

	#Sustituir el username por el email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= []

