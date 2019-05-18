from django.shortcuts import render, redirect
from django.http import HttpResponse
from product.models import Product
from product.forms import ProductForm
from django.http import JsonResponse
from rest_framework.views import APIView

from .serializers import ProductSerializer

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

def edit(request, id):
    product = Product.objects.get(id = id)
    return render(request, 'edit.html',{'product' : product})

def update(request, id):
    product = Product.objects.get(id = id)
    form = ProductForm(request.POST, instance = product)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'product': product})

def raw_sql(request):
    name = ""
    for p in Product.objects.raw('SELECT * FROM products'):
        name = name + " " + p.pname
    return JsonResponse({'result': name})

def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many = True)
    return JsonResponse(serializer.data, safe = False)

class ProductView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Product was successful.'})
        return JsonResponse({'messsage': 'Problem while adding product'})
    
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    def delete(self, request, id):
        product = Product.objects.get(id=id)
        product.delete()
        return JsonResponse({'message': 'Product Deleted'})  
