from django.db import models

# Create your models here.
class Product(models.Model):
    pro_title = models.CharField(max_length=100)
    pro_price = models.CharField(max_length=50)
    pro_description = models.CharField(max_length=200)
    pro_color = models.CharField(max_length=50)
    pro_size = models.CharField(max_length=10)
    pro_img = models.ImageField(upload_to='images')
