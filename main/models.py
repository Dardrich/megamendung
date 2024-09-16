from django.db import models
import uuid

# Create your models here.
class ProductEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    stock = models.IntegerField(default=0)