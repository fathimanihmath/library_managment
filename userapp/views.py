

# Create your views here.

from decimal import Decimal
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Cart_item
from library_app.models import Product
from datetime import datetime
from library_app.forms import DeliveryAddressForm
from .forms import PaymentForm
from django.views.decorators.csrf import csrf_exempt
from razorpay.errors import BadRequestError
from django.utils import timezone




def index(request):
    return render(request,'index.html')



@login_required
def Add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)   
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        
        # Check if the requested quantity is available
        if product.stock >= quantity:
            # Try to get the cart item for the current user and product
            try:
                cart_item = Cart_item.objects.get(product=product, user=request.user)
                # If the cart item already exists, update its quantity
                cart_item.quantity += quantity
                product.stock -= quantity 
                product.save()
                cart_item.save()
            except Cart_item.DoesNotExist:           
                # If the cart item doesn't exist, create it
                Cart_item.objects.create(product=product, quantity=quantity, user=request.user, created_at=timezone.now())
                
            # Redirect the user to the cart page
            return redirect('cart')
        else:
            # Redirect the user to the product page with a message indicating insufficient stock
            messages.error(request, f"Insufficient stock available. Available stock: {product.stock}")
            # return redirect('add_to_cart', product_id=product_id)
            return render(request, 'product.html',{'product': product})
            
    else:
        return render(request, 'product.html', {'product': product})
    



from django.contrib import messages


def update_cart_quantity(request, cart_item_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        cart_item = Cart_item.objects.get(id=cart_item_id)
        cart_item.quantity = quantity
        cart_item.save()
        messages.success(request, 'Cart item quantity updated successfully.')
    return redirect('cart')  # Redirect to the cart page

# views.py

def remove_cart_item(request, cart_item_id):
    if request.method == 'POST':
        cart_item = Cart_item.objects.get(id=cart_item_id)
        cart_item.delete()
        messages.success(request, 'Cart item removed successfully.')
    return redirect('cart')  # Redirect to the cart page
 

    
@login_required
def cart(request):
    cart_items = Cart_item.objects.filter(user=request.user)
    total_price = 0
    total_quantity = 0
    sub_total = {}
    for cart_item in cart_items:
            cart_item.subtotal = cart_item.product.price * cart_item.quantity       
            total_price += cart_item.subtotal 
            total_quantity += cart_item.quantity
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price, 'total_quantity': total_quantity})




    
    


@login_required
def checkoutview(request):
    form=DeliveryAddressForm()
    return render(request,'checkout.html',{'form':form})




@csrf_exempt
def payment_success(request):
    allobj=Cart_item.objects.filter(user=request.user)
    allobj.delete()
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        return render(request, 'payment_success.html')  # Redirect to a success page
    else:
        form = PaymentForm()
        return render(request, 'payment.html', {'form': form})


import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest


# authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(
	auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

@login_required
def payment_view(request):
    total_price = Decimal('0.00')
    total_quantity = 0
    sub_total = {}
    cart_items = Cart_item.objects.filter(user=request.user)
    
    # Calculate total price and total quantity
    for cart_item in cart_items:
        cart_item.subtotal = cart_item.product.price * cart_item.quantity       
        total_price += Decimal(str(cart_item.subtotal)) 
        total_quantity += cart_item.quantity
    
    # Ensure total price is at least INR 1.00
    if total_price < Decimal('1.00'):
        return render(request, 'paymentfail.html')  # Render a failure page
    
    amount = total_price.quantize(Decimal('1.00'))  # Round the amount to two decimal places
    
    currency = 'INR'
    
    try:
        # Create a Razorpay order
        razorpay_order = razorpay_client.order.create(dict(
            amount=int(amount * 100),  # Convert amount to smallest currency unit (paise)
            currency=currency,
            payment_capture='0'
        ))

        # Get order ID of the newly created order
        razorpay_order_id = razorpay_order['id']
        callback_url = 'paymenthandler/'

        # Pass these details to the frontend
        context = {
            'razorpay_order_id': razorpay_order_id,
            'razorpay_merchant_key': settings.RAZOR_KEY_ID,
            'razorpay_amount': amount,
            'currency': currency,
            'callback_url': callback_url
        }

        return render(request, 'paymentpage.html', context=context)
    except BadRequestError:
        return render(request, 'paymentfail.html') 

# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.

@csrf_exempt
def paymenthandler(request):

	# only accept POST request.
	if request.method == "POST":
            try:
            
                # get the required parameters from post request.
                payment_id = request.POST.get('razorpay_payment_id', '')
                razorpay_order_id = request.POST.get('razorpay_order_id', '')
                signature = request.POST.get('razorpay_signature', '')
                params_dict = {
                    'razorpay_order_id': razorpay_order_id,
                    'razorpay_payment_id': payment_id,
                    'razorpay_signature': signature
                }

                # verify the payment signature.
                result = razorpay_client.utility.verify_payment_signature(
                    params_dict)
                if result is not None:
                    amount = 0 # Rs. 200
                    try:

                        if amount >= 1.00:# capture the payemt
                            razorpay_client.payment.capture(payment_id, amount)
                            return render(request, 'paymentsuccess.html')
                        else:
                            return render(request, 'paymentfail.html')

                    except:

                        # if there is an error while capturing payment.
                        return render(request, 'paymentfail.html')
                else:

                    # if signature verification fails.
                    return render(request, 'paymentfail.html')
            except:

                # if we don't find the required parameters in POST data
                return HttpResponseBadRequest()
            else:
        # if other than POST request is made.
                return HttpResponseBadRequest()