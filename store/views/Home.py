from django.shortcuts import render,redirect
from django.http import HttpResponse
from store.models import Product
from store.models import Category 
from store.models import Customer
from django.contrib.auth.hashers import make_password,check_password
from django.views import View


# Create your views here.


class Index(View):

    def post(self,request):

        product = request.POST.get('productId')
        cart = request.session.get('cart')
        remove = request.POST.get('remove')

        if cart :
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if(quantity<=1):
                        cart.pop(product)
                    else:
                        cart[product]= quantity -1
                else:
                    cart[product]= quantity +1
            else:
                cart[product]=1
        else:
            cart={}
            cart[product]=1

        print(product)

        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect('homepage')
        

    def get(self,request):

        cart=request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_CategoryId(categoryID)
        else:
            products = Product.get_all_products()
        data = {}
        data['products'] = products
        data['categories'] = categories


        # print(products)
        # return render(request,'orders/order.html')
        # return HttpResponse('<H1>Index Page</H1>')

        print("hello",request.session.get('email'))
        return render(request, 'index.html', data)

        # return render(request,'orders/order.html')



