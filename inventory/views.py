from django.shortcuts import render, redirect
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        quantity = request.POST['quantity']
        Product.objects.create(name=name, description=description, quantity=quantity)
        return redirect('product_list')
    return render(request, 'add_product.html')

def update_quantity(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        quantity = request.POST['quantity']
        product.quantity = quantity
        product.save()
        return redirect('product_list')
    return render(request, 'update_quantity.html', {'product': product})