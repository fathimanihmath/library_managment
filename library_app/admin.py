from django.contrib import admin
from .models import *
# admin.site.register(Product_category)
# admin.site.register(Product_inventory)
# admin.site.register(Product) 
# admin.site.register(Discount)
# admin.site.register(Payment_details)
# admin.site.register(Order_items)
# admin.site.register(Order_details)
# admin.site.register(FoodProduct)
# admin.site.register(DeliveryAddress)




class Product_categoryAdmin(admin.ModelAdmin):
    list_display=['id','name','description']
    ordering=('name',)
    search_fields=('name',)
    # exclude=['created_user']

admin.site.register(Product_category,Product_categoryAdmin)


# class Product_inventoryAdmin(admin.ModelAdmin):
#     list_display=['created_at','modified_at']
#     ordering=('created_at',)
#     search_fields=('created_at',)

# admin.site.register(Product_inventory,Product_inventoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display=['name','description','stock','category','price','created_date','modified_at','deleted_at']
    ordering=('name',)
    search_fields=('name','category','price',)

admin.site.register(Product,ProductAdmin)


class Order_itemsAdmin(admin.ModelAdmin):
    list_display=['order_id','quantity']
    ordering=('order_id',)
    search_fields=('order_id',)

admin.site.register(Order_items,Order_itemsAdmin)


class Order_detailsAdmin(admin.ModelAdmin):
    list_display=['total','delivery_address','payment_id','modified_at']
    ordering=('id',)
    search_fields=('delivery_address','payment_id',)

admin.site.register(Order_details,Order_detailsAdmin)


class DeliveryAddressAdmin(admin.ModelAdmin):
    list_display=['user','address_line1','address_line2','city','state','zip_code']
    ordering=('address_line1',)
    search_fields=('name','address',)

admin.site.register(DeliveryAddress,DeliveryAddressAdmin)


class Payment_detailsAdmin(admin.ModelAdmin):
    list_display=['order','amount','created_at']
    ordering=('order',)
    search_fields=('order',)

admin.site.register(Payment_details,Payment_detailsAdmin)