from django.db import models

# Create your models here.

class facemash(models.Model):
    
    user = models.CharField(max_length = 10)
    img = models.ImageField(upload_to = 'pics')
    rating = models.IntegerField()