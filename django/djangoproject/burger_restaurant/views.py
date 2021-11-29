from django.shortcuts import render, redirect
from django.http import HttpResponse


from .models import Customer, Order, Side_Menu, Drink_Menu
from .forms import CustomerForm, OrderForm, SideForm, DrinkForm

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
    
    Order.objects.filter(order_num=primary).delete()
    context = {"orders": Order.objects.all()
    }
    return render(request,'order.html', context) 

def menu(request):
    context = {"sides": Side_Menu.objects.all(),
            "drinks": Drink_Menu.objects.all(),
    }
    return render(request, "menu.html", context)

def createSide(request):
        
    form = SideForm()
    if request.method == 'POST':
        form = SideForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/menu/')

    context = {'form':form}
    return render(request,'addUpdateSide.html', context)

def createDrink(request):
        
    form = DrinkForm()
    if request.method == 'POST':
        form = DrinkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/menu/')

    context = {'form':form}
    return render(request,'addUpdateDrink.html', context)

def updateSide(request, primary):
    
    side = Side_Menu.objects.get(side_id=primary)
    form = SideForm(instance=side)

    if request.method == 'POST':
        form = SideForm(request.POST, instance = side)
        if form.is_valid():
            form.save()
            return redirect('/home/menu/')

    context ={'form': form}
    return render(request,'addUpdateSide.html', context) 

def updateDrink(request, primary):
    
    drink = Drink_Menu.objects.get(drink_id=primary)
    form = DrinkForm(instance=drink)

    if request.method == 'POST':
        form = DrinkForm(request.POST, instance = order)
        if form.is_valid():
            form.save()
            return redirect('/home/menu/')

    context ={'form': form}
    return render(request,'addUpdateDrink.html', context) 

def deleteSide(request, primary):
    
    Side_Menu.objects.filter(side_id=primary).delete()
    context = {"sides": Side_Menu.objects.all(),
            "drinks": Drink_Menu.objects.all(),
    }
    return render(request,'menu.html', context) 

def deleteDrink(request, primary):
    
    Drink_Menu.objects.filter(drink_id=primary).delete()
    context = {"sides": Side_Menu.objects.all(),
            "drinks": Drink_Menu.objects.all(),
    }
    return render(request,'menu.html', context) 