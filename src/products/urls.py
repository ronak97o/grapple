from django.conf.urls import url
from django.contrib import admin
from .views import (product_list_view,ProductView, order_page,success)

urlpatterns = [
    
    url(r'^$', product_list_view),
    url(r'^$', ProductView  ),
    url(r'^order/$',order_page,name="order"),
    url(r'^success/$',success,name="success")

    ]