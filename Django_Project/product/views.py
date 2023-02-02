from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    return render(request,'register.html')

def login(request):
    return render(request,'signin.html')

def dashboard(request):
    return render(request,'dashboard.html')

def cart(request):
    return render(request,'cart.html')


def place_order(request):
    return render(request,'place-order.html')

def store(request):
    return render(request,'store.html')

def signin(request):
    return render(request,'signin.html')

def reg_cart(request):
    return render(request,'cart.html')

def reg_place(request):
    return render(request,'place-order.html')

def store_singin(request):
    return render(request,'signin.html')
    
def pro_detail(request):
    return render(request,'product-detail.html')