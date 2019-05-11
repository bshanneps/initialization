from django.shortcuts import render, redirect
from django.http import HttpResponse
from product.models import Product
from product.forms import ProductForm

# Create your views here.

def show(request):
    products = Product.objects.all()
    return render(request, "show.html", {'products': products})

def product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    
    else:
        form = ProductForm()
    return render(request, 'index.html', {'form': form})

def destroy(request, id):
    product = Product.objects.get(id = id)
    product.delete()
    return redirect("/show")

def change(request, id):
    if request.method == "GET":
        form = ProductForm(request.GET)
        print("happy")
        product = Product.objects.get(id = id)
        product.edit()
    return redirect("/show")
       