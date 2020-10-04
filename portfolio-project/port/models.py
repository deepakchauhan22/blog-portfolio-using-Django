from django.db import models

# Create your models here.
class Port(models.Model):

    image =models.ImageField(upload_to = 'images/')
    summmary = models.CharField(max_length=200)

    def __str__(self):
        return self.summmary
   
