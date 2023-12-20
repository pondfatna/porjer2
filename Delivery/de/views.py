from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from de.models import Product
from .forms import CustomUserCreationForm, CustomAuthenticationForm, OrderForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'de/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('product_list')  # Redirect to the home page or dashboard
    else:
        form = CustomAuthenticationForm()
    return render(request, 'de/login.html', {'form': form})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'de/product_list.html', {'products': products})

def order_product(request, product_id):
    product = Product.objects.get(pk=product_id)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            # ทำการประมวลผลการสั่งซื้อที่นี่
            # ตัวอย่าง: บันทึกลงในฐานข้อมูล, ส่งอีเมลแจ้งเตือน, แล้ว redirect กลับไปที่หน้ารายการสินค้า
            return redirect('product_list')
    else:
        form = OrderForm()

    return render(request, 'de/order_product.html', {'product': product, 'form': form})
