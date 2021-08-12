from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
# Create your models here.

class Stays(models.Model):
    pgid =  models.CharField(max_length=25,blank=False)
    Name = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    cost = models.CharField(max_length=6)
    rating = models.IntegerField(default = 0,validators=[MaxValueValidator(5), MinValueValidator(0)])
    photo = models.ImageField(upload_to = 'media/preview')

    def __str__(self):
        return self.Name


class FeaturedCard(models.Model):
    pgid = models.ForeignKey(Stays , default=None, on_delete=CASCADE)
    
    def __str__(self):
        return str(self.pgid)

