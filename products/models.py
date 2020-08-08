from django.db import models
from django.utils import timezone
import uuid

# Create your models here.

class Category(models.Model):
    id = models.UUIDField( 
        primary_key = True, 
        default = uuid.uuid4, 
        editable = False) 
    category_name=models.CharField(max_length=20,unique=True)
    description=models.TextField(max_length=100)
    category_image=models.ImageField(upload_to='categories/')
    created_at=models.DateField(default=timezone.now)

    class Meta():
        ordering=['-created_at']
        verbose_name_plural = 'Categories' 
    
    def __str__(self):
        return self.category_name

class Company(models.Model):
    id = models.UUIDField( 
        primary_key = True, 
        default = uuid.uuid4, 
        editable = False) 
    company_name=models.CharField(max_length=10,unique=True)
    company_logo=models.ImageField(upload_to='company/')

    class Meta():
        verbose_name_plural = 'Companies'
    
    def __str__(self):
        return self.company_name

class Product(models.Model):
    id = models.UUIDField( 
        primary_key = True, 
        default = uuid.uuid4, 
        editable = False) 
    name=models.CharField(max_length=30,unique=True)
    product_image=models.ImageField(upload_to='products/')
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    detail_text=models.TextField(max_length=300)
    launch_date=models.DateField()
    onsale=models.BooleanField(default=True)
    price=models.PositiveIntegerField()
    is_bestseller=models.BooleanField(default=False)

    class Meta:
        ordering=['-launch_date']
        verbose_name_plural = 'Products' 
    
    def __unicode__(self):
        return self.product_name



    
    


