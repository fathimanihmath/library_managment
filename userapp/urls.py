from django.urls import path
from .import views
from .views import payment_view

app_name='userapp'

urlpatterns = [
    path('',views.index,name="home"),
    path('product/<int:product_id>',views.Add_to_cart,name='add_to_cart'),
    
   
]
