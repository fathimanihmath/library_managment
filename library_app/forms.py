from django import forms
from .models import DeliveryAddress

class DeliveryAddressForm(forms.ModelForm):

    class Meta:
        model=DeliveryAddress
        fields=['address_line1','address_line2','city','state','zip_code']