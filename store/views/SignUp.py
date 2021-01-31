from django.shortcuts import render,redirect
from django.http import HttpResponse
from  store.models import Product
from store.models import Category 
from store.models import Customer
from django.contrib.auth.hashers import make_password,check_password
from django.views import View




class SignUp(View):
    def get(self,request):
        return render(request, 'signup.html')
   
   
    def post(self,request):

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

        err_msg= self.validateCustomer(customer)


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

    def validateCustomer(self,customer):
        err_msg= None
        if (not customer.password):
            err_msg = "Password required"

        elif customer.password:
            if (len(customer.password) < 6):
                err_msg = "Password size must be greater than 6"
        if customer.isExists():
            err_msg = "Email Address already registerd"

        return err_msg


