from pyexpat import model
from django.db import models


class Product(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=10)
    image = models.ImageField(upload_to='images')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
