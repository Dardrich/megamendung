from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField() # Harga tiap produk dipastikan bilangan bulat
    description = models.TextField()