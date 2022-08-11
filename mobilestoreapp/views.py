from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import *

# Create your views here.

def fun(request,c_slug=None):
    c_page=None
    prodt=None
    if c_slug!=None:
        c_page=get_object_or_404(Brand_nm,slug=c_slug)
        prodt=product.objects.filter(brand_name=c_page)
    else:
        prodt=product.objects.all().filter()
    br=Brand_nm.objects.all()
    return render(request,'index.html',{'prodt':prodt,'br':br})

def prodDetails(request,c_slug,product_slug):
    try:
        prod=product.objects.get(brand_name__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'item.html',{'pr':prod})

def searching(request):
    prod=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        prod=product.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))
    return render(request,'search.html',{'qr':query,'pr':prod})

def register(request):
    if request.method=='POST':
        username=request.POST['usrnm']
        email = request.POST['email']
        password1 = request.POST['psw1']
        password2 = request.POST['psw2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email)
                user.save();
                print("user created")
            return redirect('/')
        else:
            # print("password not matched")
            messages.info(request,"password not matched")
            return redirect('register')
    else:
        return render(request,'register.html')

def login(request):
    if request.method=="POST":
        username=request.POST['usrnm']
        password = request.POST['psw1']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid details')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
