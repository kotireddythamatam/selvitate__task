from django.db import models

# Create your models here.
class FILE(models.Model):
    Product_Name = models.CharField(max_length=264,blank=True,null=True)
    Product_URL = models.URLField(verbose_name=None,blank=True,null=True)
    Reviews = models.CharField(max_length=64,blank=True,null=True)
    Review_Count = models.CharField(max_length=64,blank=True,null=True)
    Price = models.CharField(max_length=64,blank=True,null=True)
    Image_URL = models.URLField(verbose_name=None,blank=True,null=True)
    Category = models.CharField(max_length=64,blank=True,null=True)
    Sub_Category = models.CharField(max_length=64,blank=True,null=True)

    def __str__(self):
        return self.Price
