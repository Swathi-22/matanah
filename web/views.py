from django.shortcuts import render

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
    context = {

    }
    return render(request,'web/product.html',context)


def contact(request):
    context = {

    }
    return render(request,'web/contact.html',context)