"""pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
# import django
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from homepage.views import home


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',home),
    url(r'^home/', include("homepage.urls",namespace="home")),
    url(r'^contact/', include("contact.urls")),
    url(r'^login/', include("login.urls",namespace='login')),
    url(r'^register/', include("register.urls",namespace="register")),
     url(r'^placeorders/', include("placeorders.urls",namespace="kamal")),
    # url(r'^cart/', include("cart.urls",namespace="cart")),
    # url(r'^cart/', include("carts.urls", namespace='carts')),
   
    url(r'^product-fun/', include('products.urls',namespace="prod")),
    # url(r'^kamal/$', include('jam.urls')),

    # url(r'^order_page/', include("place_order.urls")),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
