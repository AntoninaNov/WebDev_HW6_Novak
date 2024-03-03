"""
URL configuration for nobel_laureates_endpoints project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.urls import include, path
from . import views

urlpatterns = [
    path('', include('nobels.urls')),
    path('cookie/set', views.set_cookie_view, name='set_cookie'),
    path('cookie/get/<key>', views.get_cookie_view, name='get_cookie'),
    path('header/set', views.set_header_view, name='set_header'),
    path('header/get/<key>', views.get_header_view, name='get_header'),
]

# To set a cookie: http://127.0.0.1:8000/cookie/set?key=my&value=favorite
# To get a cookie: http://127.0.0.1:8000/cookie/get/my
# To set a header: http://127.0.0.1:8000/header/set?key=headerName&value=headerValue
# To get a header: http://127.0.0.1:8000/header/get/headerName
# (please add the header to the Postman request in Headers section)
