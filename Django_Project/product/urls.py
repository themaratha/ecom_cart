from django.contrib import admin
from django.urls import path,include
from product.views import index,register,login,dashboard,cart,place_order,store,signin,reg_cart,reg_place,store_singin,pro_detail

urlpatterns = [
    path('',index,name='index'),
    path('register/',register, name='register'),
    path('login/',login, name='login'),
    path('dashboard/',dashboard, name='dashboard'),
    path('cart/',cart, name='cart'),
    path('cart/place-order.html/',place_order, name='place_order'),
    path('cart/store.html/',store, name='store'),
    path('register/signin.html',signin,name='signin'),
    path('register/cart.html',reg_cart,name='reg_cart'),
    path('register/place-order.html',reg_place,name='reg_place'),
    path('cart/store.html/signin.html',store_singin,name='store_singin'),
    path('store.html/',store,name='store'),
    path('store.html/signin.html',signin,name='signin'),
    path('signin.html',login,name='login'),
    path('product-detail.html',pro_detail,name='pro_detail'),


]