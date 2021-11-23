from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add_customer/', views.createCustomer, name="add_customer"),
    path('update_customer/<str:primary>/', views.updateCustomer, name = "update_customer" )
]
