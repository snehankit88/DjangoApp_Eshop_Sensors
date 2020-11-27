from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from django.contrib.auth.hashers import make_password,check_password
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


def validateCustomer(customer):
    err_msg= None
    if (not customer.password):
        err_msg = "Password required"

    elif customer.password:
        if (len(customer.password) < 6):
            err_msg = "Password size must be greater than 6"
    if customer.isExists():
        err_msg = "Email Address already registerd"

    return err_msg



def registerUser(request):

    postData  = request.POST
    email = postData.get('email')
    fname = postData.get('fname')
    lname = postData.get('lname')
    pwd = postData.get('password')
    phone = postData.get('phone')

    #Validation

    value = {
        'fname':fname,
        'lname':lname,
        'phone':phone,
        'email':email

    }


    err_msg = None
    customer = Customer(first_name=fname, last_name=lname, email=email, password=pwd, phone=phone)

    err_msg=validateCustomer(customer)


    #saving
    if not err_msg:
        customer.password = make_password(customer.password)
        customer.register()
        return redirect('homepage')
    else:
        data={
            'error':err_msg,
            'values':value
        }
        print("already",err_msg)
        return  render(request,'signup.html',data)

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else :
        return registerUser(request)
