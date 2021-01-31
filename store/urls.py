
from django.contrib import admin
from django.urls import path

from  store.views import Home,SignUp,Login,Cart


urlpatterns = [
    path('',Home.Index.as_view(),name='homepage'),
    path('signup',SignUp.SignUp.as_view(),name='SignUp'),
    path('login',Login.Login.as_view(),name='Login'),
    path('logout',Login.logout,name='logout'),
    path('cart',Cart.Cart.as_view(),name='cart')
]
