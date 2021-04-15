from django.urls import path

from . import views
from .views import Home, TestPayment

app_name = 'frontend'

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('paystack/', TestPayment.as_view(), name="home"),
    path('verify/nin/', views.post_nin, name='post_nin'),
    path('verify/phone/', views.post_phone, name='post_phone'),
    path('verify/demo/', views.post_demo, name='post_demo'),
]
