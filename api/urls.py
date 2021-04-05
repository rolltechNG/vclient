"""vericlient URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt

# from ../ import views
from api import views


urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('nin/<str:token>/<str:nin>',
         views.nin_verification_vw, name="nin_verification"),
    path('phone/<str:token>/<str:phone>',
         views.phone_verification_vw, name="phone_verification"),
    path('doc/<str:token>/<str:doc>',
         views.doc_verification_vw, name="doc_verification"),
    path('demo/<str:token>/<str:firstname>/<str:lastname>/<str:dob>',
         views.demo_verification_vw, name="demo_verification"),
    #     path('fingersearch/<str:token>/<str:data>/<str:pos>',
    #          views.finger_search_vw, name="fingersearch"),
    path('fsearch/<str:token>',
         views.finger_search_vw, name="fingersearch"),
    path('fingerverification/<str:token>/<str:nin>',
         csrf_exempt(views.finger_verification_vw), name="fingerverification"),
    path('photoverification/<str:token>/<str:nin>/',
         views.photo_verification_vw, name="photoverification"),


    #     path('f/<str:token>',
    #          views.finger_search_vw00, name="fingersearch00"),

]
