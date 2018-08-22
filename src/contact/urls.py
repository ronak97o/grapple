from django.conf.urls import url
from django.contrib import admin
from .views import (contact)

urlpatterns = [
    
    url(r'^$', contact)
    ]