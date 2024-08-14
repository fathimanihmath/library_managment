from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from library_app.models import Master,Product
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.

    
class User_address(Master):
    address_line1 = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=100,blank=True,null=True)
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    telephone = models.CharField(max_length=15)
    mobile = models.CharField(max_length=15)

    class Meta:
        verbose_name_plural='User Address'
    def __str__(self):
        return self.address_line1

class Cart_item(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_column='product_id')
    quantity = models.IntegerField()
    created_at=models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True)


    
    class Meta:
        verbose_name_plural='Cart Items'

    def __str__(self):
        return str(self.product)
    
    

        
class User_payment(Master):
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=50)
    provider = models.CharField(max_length=50)
    account_no = models.CharField(max_length=50)
    expiry = models.DateTimeField()

    class Meta:
        verbose_name_plural='User Payment'
    def __str__(self):
        return self.payment_type
    
