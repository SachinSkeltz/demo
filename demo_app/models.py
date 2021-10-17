from django.db import models

# Create your models here.
class featured_items(models.Model):
    img=models.ImageField(upload_to='picture')
    name=models.CharField(max_length=100)
    desc=models.TextField(max_length=600)