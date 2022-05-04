import code
from django.shortcuts import render
from django.http import Http404
from .models import Product
from django.contrib.auth.decorators import login_required

@login_required
def products(request):
    if 'q' in request.GET:
        q = request.GET['q']
        products = Product.objects.filter(title__icontains=q)
    else:
        products = Product.objects.all()
    
    return render(request, 'products/products.html', {'products': products})

@login_required
def details(request, product_id):
    try:
        products = Product.objects.get(id=product_id)
    except:
        raise Http404("Product not found")

    return render(request, 'products/details.html', {'products': products})
