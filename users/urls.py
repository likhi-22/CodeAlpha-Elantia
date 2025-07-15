from django.urls import path
from . import views, views_index, views_home, views_cart, views_orders

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views_home.home, name='home'),
    path('cart/', views_cart.cart, name='cart'),
    path('orders/', views_orders.orders, name='orders'),
    path('location/', views.location, name='location'),
    path('', views_index.index, name='index'),
]
