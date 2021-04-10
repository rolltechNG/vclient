from django.urls import path

from . import views
from .views import Home

app_name = 'frontend'

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('verify/nin/', views.post_nin, name='post_nin')
]
