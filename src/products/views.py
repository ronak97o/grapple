from django.shortcuts import render,redirect
# from django.views import *
from django.views.generic import ListView
from .forms import OrderForm
from .models import Product,Order
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
class ProductView(ListView):
    queryset = Product.objects.all()


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list' : queryset
    }
    return render(request,"products/product_list_view.html",context)

def order_page(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user= request.user
        instance.save()
        user_obj = User.objects.get(username=request.user)
        email = user_obj.email
        firstname = user_obj.first_name
        subject = "Orderconfirm : Grapple"
        to_email = [email]
        contact_message = "this is a message from Grapple : {} regarding : {} to: ".format(email,
                                                                                  firstname)
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, from_email, contact_message, to_email, fail_silently=False)
        return redirect("prod:success")
    context={
        "form":form
    }    
    return render(request,"order.html",context)

def success(request):
    return render(request,"placeorders/success.html",{})