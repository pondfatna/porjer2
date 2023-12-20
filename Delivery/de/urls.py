# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('product_list/', product_list, name='product_list'),
     path('order_product/<int:product_id>/', order_product, name='order_product'),

]
