
from django import forms
from .models import User_payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = User_payment
        fields = ['payment_type','provider','account_no','expiry']