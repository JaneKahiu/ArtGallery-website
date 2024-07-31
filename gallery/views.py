from django.shortcuts import render,redirect
from.models import Product
from django.http import HttpResponse


# Create your views here.
def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request , 'index.html', context)