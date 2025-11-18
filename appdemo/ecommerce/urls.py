from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout,name='logout'),
    path('',views.product_list,name='product_list'),
    path('add_to_cart/<int:product_id>',views.add_to_cart,name='add_to_cart'),
    path('cart/', views.cart_page, name='cart_page'),
]