from django.shortcuts import render
from web.models import Category, Product,Gallery
# Create your views here.
def index(request):
    context = {

    }
    return render(request,'web/index.html',context)


def about(request):
    context = {

    }
    return render(request,'web/about.html',context)


def gallery(request):
    context = {

    }
    return render(request,'web/gallery.html',context)



def product(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories':categories,
        'products':products

    }
    return render(request,'web/product1.html',context)


def contact(request):
    context = {

    }
    return render(request,'web/contact.html',context)