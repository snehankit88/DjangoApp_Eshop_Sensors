from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category
from .models.customer import Customer

# Create your views here.

def index(request):
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

    return render(request, 'index.html', data)

    # return render(request,'orders/order.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        postData  = request.POST

        email = postData.get('email')
        fname = postData.get('fname')
        lname = postData.get('lname')
        pwd = postData.get('password')
        phone = postData.get('phone')

        #Validation
        err_msg = None

        if(not pwd):
            err_msg = "Password requuired"

        elif pwd:
            if(len(pwd)<6):
                err_msg = "Password size must be greater than 6"


        if not err_msg:
            customer = Customer(first_name = fname,last_name = lname,email= email, password = pwd,phone = phone )
            customer.register()
        else:
            return  render(request,'signup.html',{'error':err_msg})