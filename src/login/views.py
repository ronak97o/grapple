from django.contrib.auth import authenticate,login,get_user_model,logout
from django.http import HttpResponse
from django.shortcuts import render,redirect

from .forms import LoginForm
# Create your views here.
def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    print("User logged in")
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        print(user)
        # print(request.user.is_authenticated())
        if user is not None:
            # print(request.user.is_authenticated())
            login(request, user)
            # Redirect to a success page.
            # context['form'] = LoginForm()
            return redirect("home:homepage")
        else:
            # Return an 'invalid login' error message.
            print("Error")

    return render(request, "login/login.html", context)

def logout_page(request):
   logout(request)
   return redirect('login:home')