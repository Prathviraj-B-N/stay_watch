from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
from ckeditor.fields import RichTextField
# Create your models here.

class landlord(models.Model):
    name = models.CharField(max_length = 20)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


class Stays(models.Model):
    name = models.CharField(max_length=25)
    cost = models.CharField(max_length=6)
    rating = models.IntegerField(default = 0,validators=[MaxValueValidator(5), MinValueValidator(0)])
    photo = models.ImageField(upload_to = 'media/preview')
    addr_line1 = models.CharField(max_length=50)
    addr_line2 = models.CharField(max_length=50)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    description = RichTextField()
    owner = models.ForeignKey(landlord , default=None, on_delete=SET_NULL , null=True)
    isFeatured = models.BooleanField(default=False)


    def __str__(self):
        return self.name


class tenant(models.Model):
    name = models.CharField(max_length = 20)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    stay = models.ForeignKey(Stays,default=None, on_delete=SET_NULL,null=True,blank=True)

    def __str__(self):
        return str(self.name)


