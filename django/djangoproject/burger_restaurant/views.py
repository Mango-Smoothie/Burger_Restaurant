from django.shortcuts import render, redirect
from django.http import HttpResponse


from .models import Customer, Order, Side_Menu, Drink_Menu
from .forms import CustomerForm, OrderForm

def home(request):
    return render(request, "home.html")

def customer(request):
    context = {"customers": Customer.objects.all()
    }
    return render(request, "customer.html", context)

def createCustomer(request):
        
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/customer/')

    context = {'form':form}
    return render(request,'addUpdateCustomer.html', context) 

def updateCustomer(request, primary):
    
    customer = Customer.objects.get(id=primary)
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance = customer)
        if form.is_valid():
            form.save()
            return redirect('/home/customer/')

    context ={'form': form}
    return render(request,'addUpdateCustomer.html', context) 

def deleteCustomer(request, primary):
    

    Customer.objects.filter(id=primary).delete()
    context = {"customers": Customer.objects.all()
    }
    # if request.method =="POST":
    #     customer.delete()
    #     return redirect('/home/customer/')
    return render(request,'customer.html', context) 


def order(request):
    context = {"orders": Order.objects.all()}
    # return HttpResponse("Hello, world. You're at the Burger Restaurant index.")
    return render(request, "order.html", context)\

def createOrder(request):
        
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/order/')

    context = {'form':form}
    return render(request,'addUpdateOrder.html', context)

def updateOrder(request, primary):
    
    order = Order.objects.get(order_num=primary)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance = order)
        if form.is_valid():
            form.save()
            return redirect('/home/order/')

    context ={'form': form}
    return render(request,'addUpdateOrder.html', context) 


def deleteOrder(request, primary):
    
    order = Order.objects.get(order_num=primary)
    if request.method =="POST":
        order.delete()
        return redirect('/home/order/')
    context ={'order': order}
    return render(request,'deleteOrder.html', context) 

def menu(request):
    context = {"sides": Side_Menu.objects.all(),
            "drinks": Drink_Menu.objects.all(),
    }
    return render(request, "menu.html", context)