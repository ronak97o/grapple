from django.conf.urls import url
from django.contrib import admin
from .views import register_page
appname = "register"
urlpatterns = [
    
    url(r'^$', register_page,name="r")
    ]