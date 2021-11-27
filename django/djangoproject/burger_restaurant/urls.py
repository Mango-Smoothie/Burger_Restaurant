from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    
    path('customer/', views.customer, name = "customer" ),
    path('add_customer/', views.createCustomer, name="add_customer"),
    path('update_customer/<str:primary>/', views.updateCustomer, name = "update_customer" ),
    
    # path('order/', views.order, name = "order" )
]
