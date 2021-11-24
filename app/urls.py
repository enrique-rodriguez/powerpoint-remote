from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('send_key/', views.send_key, name="send_key"),
]