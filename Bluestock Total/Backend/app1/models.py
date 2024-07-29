from django.db import models

# Create your models here.
class Item(models.Model):
    box = models.CharField(max_length=6,default='')
    name = models.CharField(max_length=255,default='Not Issued')
    Brand = models.CharField(max_length=255,default='Not Issued')
    Price_Band = models.CharField(max_length=100,default='Not Issued')
    Open = models.CharField(max_length=100,default='Not Issued')
    Close = models.CharField(max_length=100,default='Not Issued')
    Issue_size= models.CharField(max_length=100,default='Not Issued')
    Issue_Type= models.CharField(max_length=100,default='Not Issued')
    Listing_Date= models.CharField(max_length=100,default='Not Issued')

    def __str__(self):
      return self.name
