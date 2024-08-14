
# Create your views here.


from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product
from django.shortcuts import get_object_or_404






def index(request):
    return render(request,'index.html')
@login_required(login_url='login')


def product(request):
    products=Product.objects.all()
    return render(request,'collections.html',{'product':products})

def About(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def blog(request):
    return render(request,'blog.html')
def loginn(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid login")
            return redirect('login')

    return render(request,'login.html')

def Register(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['psw1']
        
        if User.objects.filter(email=email).exists():
            messages.info(request,"Email already exists")
            return redirect('Register')
        elif User.objects.filter(username=username).exists():
            messages.info(request,"username already exists")
            return redirect('Register')
        else:
            user=User.objects.create_user(username=username,email=email,password=password)  
            user.save()
            return redirect('login')
    else:
        return render(request,'Register.html')

def logout(request):
    auth.logout(request)
    return redirect('login')









