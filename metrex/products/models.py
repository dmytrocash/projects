from pyexpat import model
from django.db import models

# Create your models here.

class Product(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=10)
    image = models.ImageField(upload_to='images')
    description = models.TextField()

    def __str__(self):
        return self.title