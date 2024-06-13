from django.shortcuts import render
from .models import Product

#create your views here
def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request,'ricky/product_list.html',context)