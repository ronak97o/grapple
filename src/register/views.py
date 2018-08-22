from django.conf import settings
from django.contrib.auth import authenticate,login,get_user_model
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.core.mail import send_mail

# Create your views here.
User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form" : form

    }
    if form.is_valid():
        # print(form.cleaned_data)
        firstname = form.cleaned_data.get("firstname")
        lastname = form.cleaned_data.get("lastname")
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        subject ="Site Grapple"
        to_email = [email]
        contact_message = "this is a message from: {} regarding : {} to: ".format(email,
                                                                                    firstname)
        from_email =settings.EMAIL_HOST_USER



        new_user = User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
        print(new_user)
        send_mail(subject, from_email, contact_message, to_email, fail_silently=False)
        return redirect('home:homepage')
    return render(request, "register/index.html", context)