from django.db import models
from django.contrib.auth.models import User


class Master(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    isactive = models.BooleanField(default=True,verbose_name="Active")
    created_user = models.ForeignKey(User,blank=True,on_delete=models.CASCADE)

    class Meta:
        abstract = True
        ordering = ['-isactive']


class Product_category(Master):
    name = models.CharField(max_length=30,null=True)
    description = models.TextField()
    modified_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='Product Categories'
    def __str__(self):
        return self.name
    


class DeliveryAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address_line1 = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user.username}'s address"


class Order_details(Master):
    total = models.DecimalField(max_digits=10,decimal_places=2)
    delivery_address = models.ForeignKey(DeliveryAddress, on_delete=models.CASCADE)
    payment_id = models.IntegerField()
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural='Order Details'
    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

    
class Payment_details(Master):
    order = models.OneToOneField(Order_details,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    provider = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural='Payment Details'
    def __str__(self):
        return f"Payment for order #{self.order.id}"








class Product(Master):
    name = models.CharField(max_length=200)
    description = models.TextField()
    stock = models.IntegerField(null=True) 
    category = models.ForeignKey(Product_category,on_delete=models.CASCADE)
    # inventory = models.ForeignKey(Product_inventory,on_delete=models.CASCADE,primary_key=True)
    price = models.IntegerField()
    image = models.ImageField(null=True,blank=True)
    # discount = models.ForeignKey(Discount,on_delete=models.CASCADE)
    modified_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='Product'
    def __str__(self):
        return self.name
    


        
class Order_items(Master):
    order_id = models.ForeignKey(Order_details,on_delete=models.CASCADE,related_name='order_items')
    Product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural='Order Items'

    def __str__(self):
        return f"Order #{self.id} x {self.Product_id.name} in order #{self.order_id}"

    