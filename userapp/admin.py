from django.contrib import admin
from .models import *
# Register your models here.
class User_addressAdmin(admin.ModelAdmin):
    list_display=['address_line1','address_line2','postal_code','country','telephone','mobile']
    ordering=('address_line1',)
    search_fields=('address_line1','postal_code',)

admin.site.register(User_address,User_addressAdmin)

class User_paymentAdmin(admin.ModelAdmin):
    list_display=['payment_type','provider','account_no','expiry']
    ordering=('account_no',)
    search_fields=('account_no','payment_type',)

admin.site.register(User_payment,User_paymentAdmin)
