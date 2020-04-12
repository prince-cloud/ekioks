from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
# Create your models here.

class Product(models.Model):

    CONDITION_TYPE = (
        ("New", "New"),
        ("Used", "Used"),
        ("Slightly Used", "Slightly Used")
    )

    REGION = (
        ("Ahafo Region", "Ahafo Region"),
        ("Ashante Region", "Ashante Region"),
        ("Bono Region", "Bono Region"),
        ("Bono East Region", "Bono East Region"),
        ("Central Region", "Central Region"),
        ("Eastern Region", "Eastern Treson"),
        ("Greater Accra", "Greater Accra"),
        ("Northern REgion", "Northern Region"),
        ("North East", "North East"),
        ("Oti Region", "Oti Region"),
        ("Savannah Region", "Savannah Region"),
        ("Upper East Region", "Upper East Region"),
        ("Upper West Region", "Upper West Region"),
        ("Volta Region", "Volta Region"),
        ("Western Region", "Western Region"),
        ("Western North", "Western North")
    )

    title = models.CharField(max_length=100)
    owner = models.ForeignKey(User , on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null = True)
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null = True, blank=True )
    description = models.TextField(max_length=500)
    condition = models.CharField(max_length=100, choices=CONDITION_TYPE, default="New")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    #image = models.ImageField(upload_to='main_products/', blank=True, null=True)
    phone = models.CharField(max_length=10, default=None)
    region = models.CharField(choices=REGION, max_length=50)
    date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, null=True)

    image = ProcessedImageField(upload_to='main_products/', processors=[ResizeToFill(100,100)], format='JPEG', options={'quality': 60}, blank=True, null=True)

    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(100,100)], format='JPEG', options={'quality': 60})

    class Meta:
        ordering = ('-date',)

    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)


    def __str__(self):
        return self.title


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category/', blank=True, null=True)

    slug = models.SlugField(blank=True, null=True) 
    
    def save(self, *args, **kwargs):
        if not self.slug and self.category_name:
            self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name

class Brand(models.Model):
    brand_name = models.CharField(max_length=50) 

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'
        
    def __str__(self):
        return self.brand_name


