from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import RegistrationForm, LoginForm, ProductForm
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

@staff_member_required
def admin_page(request):
    main_products = Product.objects.filter(is_main=True)
    top_products = Product.objects.filter(is_top=True)
    return render(request, 'admin_page.html', {'main_products': main_products, 'top_products': top_products})
