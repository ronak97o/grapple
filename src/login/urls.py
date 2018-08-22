from django.conf.urls import url
from django.contrib import admin
from .views import (login_page, logout_page)

app_name = 'login'
urlpatterns = [

    url(r'^$', login_page, name="home"),
    url(r'^logout/$', logout_page, name="home1"),

]