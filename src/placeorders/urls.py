from django.conf.urls import url
from django.contrib import admin
from .views import (place_order)
app_name=  'placeorders'
urlpatterns = [
   
    url(r'^$', place_order,name="k")
    ]