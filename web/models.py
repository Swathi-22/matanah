from django.db import models
from versatileimagefield.fields import VersatileImageField,PPOIField
from tinymce.models import HTMLField
# Create your models here.



class Category(models.Model):
    title =models.CharField(max_length=225)
    is_active=models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = ("Categories")

    def __str__(self):
        return str(self.title)


class Product(models.Model):
    title=models.CharField(max_length=225)
    price=models.FloatField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image = VersatileImageField('Image',upload_to='product/',ppoi_field='ppoi')
    ppoi = PPOIField('Image PPOI')
    is_popular=models.BooleanField(default=False)
    slug=models.SlugField(unique=True)


    def __str__(self):
        return self.title


class Gallery(models.Model):
    image = VersatileImageField('Image',upload_to='gallery/',ppoi_field='ppoi')
    ppoi = PPOIField('Image PPOI')

    class Meta:
        verbose_name_plural = ("Gallery")

    def __str__(self):
        return str(self.image)


class Contact(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=50)
    feedback=HTMLField(blank=True, null=True)

    def __str__(self):
        return self.firstname