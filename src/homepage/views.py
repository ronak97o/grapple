from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# from ..login.forms import LoginForm
from django.contrib.auth.models import User
# from .forms import CityForm
def home(request):
    # context = {
    #     "title" : "hello",
    #     "content" : "welcome to home page yeah"
    # }
    # form = LoginForm(request.POST or None)
    # context = {
    #     "form": form
    # }
    # print("User logged in")
    # # print(request.user.is_authenticated())
    # if form.is_valid():
    #     print(form.cleaned_data)
    #     username = form.cleaned_data.get("username")
    #     password = form.cleaned_data.get("password")
    #     user = authenticate( username=username, password=password)
    #     print(user)
    # if request.user.is_authenticted():
    #     context['prime'] = "YEAHHHHHHHHH"
    # return render(request, "home/home.html",context)
    # form = CityForm(request.POST or None)
    # name = request.user
    context = {

        "content": " Welcome to the homepage.",
        # "form" : form
    }

    if request.user.is_authenticated():
        context["prime"] = "Welcome back"

    return render(request, "home/home.html", context)

