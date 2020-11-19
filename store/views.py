from django.shortcuts import render
from django.http import HttpResponse
from .models.product import  Product
from .models.category import  Category


# Create your views here.

def index(request):
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_CategoryId(categoryID)
    else:
        products = Product.get_all_products()
    data={}
    data['products'] = products
    data['categories'] = categories

    #print(products)
   #return render(request,'orders/order.html')
    # return HttpResponse('<H1>Index Page</H1>')

    return render(request, 'index.html',data)


    #return render(request,'orders/order.html')