from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from .forms import OrderForm

def home(request):
    categories = Category.objects.all()
    return render(request, 'app3/home.html',{'categories': categories})

def catalog(request):
    categories = Category.objects.all()
    return render(request, 'app3/catalog.html', {'categories': categories})

def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.filter(available=True)
    return render(request, 'app3/category/_products.html', {'category': category, 'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id, available=True)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'app3/order/_success.html', {'product': product})
    else:
        form = OrderForm(initial={'product': product})

    return render(request, 'app3/product/_detail.html', {'product': product, 'form': form})
