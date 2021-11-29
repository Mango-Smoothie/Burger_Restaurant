from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    
    path('customer/', views.customer, name = "customer" ),
    path('add_customer/', views.createCustomer, name="add_customer"),
    path('update_customer/<str:primary>/', views.updateCustomer, name = "update_customer" ),
    path('delete_customer/<str:primary>/', views.deleteCustomer, name = "delete_customer" ),

    path('order/', views.order, name = "order" ),
    path('add_order/', views.createOrder, name="add_order"),
    path('update_order/<str:primary>/', views.updateOrder, name = "update_order" ),
    path('delete_order/<str:primary>/', views.deleteOrder, name = "delete_order" ),

    path('menu/', views.menu, name = "menu" ),

]
