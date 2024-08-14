from django.urls import path
from.import views
from django.contrib import admin
from django.conf.urls.static import static
from userapp.views import cart,Add_to_cart,checkoutview, payment_view,paymenthandler,payment_success,remove_cart_item,update_cart_quantity


urlpatterns = [
     path('',views.index,name='home'),
     path('collections',views.product,name='collections'),
      path('product/<int:product_id>',Add_to_cart,name='add_to_cart'),
     path('about/',views.About,name="about"),
     path('contact/',views.contact,name="contact"),
     path('blog/',views.blog,name="blog"),
     path('login/',views.loginn,name="login"),
     path('Register/',views.Register,name="Register"),
     path('logout/',views.logout,name="logout"),
     path('cart',cart,name="cart"),
     path('checkout',checkoutview,name="checkout"),
     path('paymenthandler/', paymenthandler, name='paymenthandler'),
     path('payment_view/', payment_view, name='payment_view/'),
     path('payment_view/paymenthandler/', payment_success,name='payment_success'),
     
     path('update_cart_quantity/<int:cart_item_id>/', update_cart_quantity, name='update_cart_quantity'),
     path('remove_cart_item/<int:cart_item_id>/', remove_cart_item, name='remove_cart_item'),

     
     ]