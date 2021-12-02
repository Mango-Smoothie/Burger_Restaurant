from django.shortcuts import render, redirect
from django.http import HttpResponse


from .models import *
from .forms import *

def main(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if Customer.objects.filter(name = request.POST['name'], phone_num = request.POST['phone_num']).exists():
            customer = Customer.objects.get(name = request.POST['name'], phone_num = request.POST['phone_num'])
            return redirect('/main/customer_home/' + str(customer.id) + '/')

    context = {'form':form}
    return render(request, "customerLogin.html", context)

def home(request, primary):

    if request.method == 'POST':
        currentorder = Order.objects.create(order_status = 'Not Started', total_price = 0, customer=Customer.objects.get(id=primary))
        currentorder.save()
        return redirect('/main/place_order/'+ str(currentorder.order_num) + '/')

    context = {
        "customer":Customer.objects.get(id=primary),
    }
    return render(request, "customerHome.html", context)


# def customer(request):
#     context = {"customers": Customer.objects.all()
#     }
#     return render(request, "customer.html", context)

def createCustomer(request):
        
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/main/')

    context = {'form':form}
    return render(request,'addUpdateCustomer.html', context) 

def placeOrder(request, primary):
    currentOrder = Order.objects.get(order_num=primary)

    sideForm = SideOrderForm(initial={'order_number': currentOrder.order_num})
    drinkForm = DrinkOrderForm(initial={'order_number': currentOrder.order_num})
    burgerForm = BurgerOrderForm(initial={'order_number': currentOrder.order_num})

    if request.method == 'POST':
        sideForm = SideOrderForm(request.POST)
        drinkForm = DrinkOrderForm(request.POST)
        burgerForm = BurgerOrderForm(request.POST)
        # sideForm = SideOrderForm(initial={'order_number': currentOrder.order_num})
        # drinkForm = DrinkOrderForm(initial={'order_number': currentOrder.order_num})
        # burgerForm = BurgerOrderForm(initial={'order_number': currentOrder.order_num})


        if sideForm.is_valid() and drinkForm.is_valid() and burgerForm.is_valid():
            sideForm.save()
            drinkForm.save()
            burgerForm.save()
            return redirect('/main/show_order/'+ str(primary) + '/')
        
    context = {
        "sides": Side_Menu.objects.all(),
            "drinks": Drink_Menu.objects.all(),
            "veggies": Veggie_Menu.objects.all(),
            "sauces": Sauce_Menu.objects.all(),
            "patties": Patty_Menu.objects.all(),
            "buns": Buns_Menu.objects.all(),
            "sideForm": sideForm,
            "drinkForm": drinkForm,
            "burgerForm": burgerForm,
    }
    return render(request, "placeOrder.html", context)

def showOrder(request, primary):
    currentOrder = Order.objects.get(order_num = primary)
    burgerOrder = Burger_Order.objects.get(order_number = primary)
    sideOrder = Side_Order.objects.get(order_number = primary)
    drinkOrder = Drink_Order.objects.get(order_number = primary)
    
    currentOrder.total_price = burgerOrder.burger_total + sideOrder.side_total + drinkOrder.drink_total
    currentOrder.save()

    context = {
        #  "order": Order.objects.get(order_num = currentOrder.order_num),
         "order": currentOrder,
         "burgerOrder": burgerOrder,
         "sideOrder": sideOrder,
         "drinkOrder": drinkOrder,
        
    }
    return render(request, "showOrder.html", context)

def orderHistory(request, primary):
    customer = Customer.objects.get(id = primary)
    orders = Order.objects.filter(customer =customer)
    context = {
        "orders":orders,
        "customer":customer,
    }
    return render(request, "orderHistory.html", context)
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
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
        form = DrinkForm(request.POST, instance = drink)
        if form.is_valid():
            form.save()
            return redirect('/home/menu/')

    context ={'form': form}
    return render(request,'addUpdateDrink.html', context) 

def deleteSide(request, primary):
    
    Side_Menu.objects.filter(side_id=primary).delete()
    context = {"sides": Side_Menu.objects.all(),
            "drinks": Drink_Menu.objects.all(),
            "veggies": Veggie_Menu.objects.all(),
            "sauces": Sauce_Menu.objects.all(),
            "patties": Patty_Menu.objects.all(),
            "buns": Buns_Menu.objects.all(),
    }
    return render(request,'menu.html', context) 

def deleteDrink(request, primary):
    
    Drink_Menu.objects.filter(drink_id=primary).delete()
    context = {"sides": Side_Menu.objects.all(),
            "drinks": Drink_Menu.objects.all(),
            "veggies": Veggie_Menu.objects.all(),
            "sauces": Sauce_Menu.objects.all(),
            "patties": Patty_Menu.objects.all(),
            "buns": Buns_Menu.objects.all(),
    }
    return render(request,'menu.html', context) 

def createPatty(request):
        
    form = PattyForm()
    if request.method == 'POST':
        form = PattyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/menu/')

    context = {'form':form}
    return render(request,'addUpdatePatty.html', context) 

def updatePatty(request, primary):
    
    patty = Patty_Menu.objects.get(patty_id=primary)
    form = PattyForm(instance=patty)

    if request.method == 'POST':
        form = PattyForm(request.POST, instance = patty)
        if form.is_valid():
            form.save()
            return redirect('/home/menu/')

    context ={'form': form}
    return render(request,'addUpdatePatty.html', context) 

def deletePatty(request, primary):

    Patty_Menu.objects.filter(patty_id=primary).delete()
    context = {"sides": Side_Menu.objects.all(),
            "drinks": Drink_Menu.objects.all(),
            "veggies": Veggie_Menu.objects.all(),
            "sauces": Sauce_Menu.objects.all(),
            "patties": Patty_Menu.objects.all(),
            "buns": Buns_Menu.objects.all(),
    }
    return render(request,'menu.html', context) 

def createBuns(request):
        
    form = BunsForm()
    if request.method == 'POST':
        form = BunsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/menu/')

    context = {'form':form}
    return render(request,'addUpdateBuns.html', context) 

def updateBuns(request, primary):
    
    bun = Buns_Menu.objects.get(buns_id=primary)
    form = BunsForm(instance=bun)

    if request.method == 'POST':
        form = BunsForm(request.POST, instance = bun)
        if form.is_valid():
            form.save()
            return redirect('/home/menu/')

    context ={'form': form}
    return render(request,'addUpdateBuns.html', context) 

def deleteBuns(request, primary):

    Buns_Menu.objects.filter(buns_id=primary).delete()
    context = {"sides": Side_Menu.objects.all(),
            "drinks": Drink_Menu.objects.all(),
            "veggies": Veggie_Menu.objects.all(),
            "sauces": Sauce_Menu.objects.all(),
            "patties": Patty_Menu.objects.all(),
            "buns": Buns_Menu.objects.all(),
    }
    return render(request,'menu.html', context) 

def createVeggie(request):
        
    form = VeggieForm()
    if request.method == 'POST':
        form = VeggieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/menu/')

    context = {'form':form}
    return render(request,'addUpdateVeggie.html', context) 

def updateVeggie(request, primary):
    
    veggie = Veggie_Menu.objects.get(veggie_id=primary)
    form = VeggieForm(instance=veggie)

    if request.method == 'POST':
        form = VeggieForm(request.POST, instance = veggie)
        if form.is_valid():
            form.save()
            return redirect('/home/menu/')

    context ={'form': form}
    return render(request,'addUpdateVeggie.html', context) 

def deleteVeggie(request, primary):

    Veggie_Menu.objects.filter(veggie_id=primary).delete()
    context = {"sides": Side_Menu.objects.all(),
            "drinks": Drink_Menu.objects.all(),
            "veggies": Veggie_Menu.objects.all(),
            "sauces": Sauce_Menu.objects.all(),
            "patties": Patty_Menu.objects.all(),
            "buns": Buns_Menu.objects.all(),
    }
    return render(request,'menu.html', context) 

def createSauce(request):
        
    form = SauceForm()
    if request.method == 'POST':
        form = SauceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/menu/')

    context = {'form':form}
    return render(request,'addUpdateSauce.html', context) 

def updateSauce(request, primary):
    
    sauce = Sauce_Menu.objects.get(sauce_id=primary)
    form = SauceForm(instance=sauce)

    if request.method == 'POST':
        form = SauceForm(request.POST, instance = sauce)
        if form.is_valid():
            form.save()
            return redirect('/home/menu/')

    context ={'form': form}
    return render(request,'addUpdateSauce.html', context) 

def deleteSauce(request, primary):

    Sauce_Menu.objects.filter(sauce_id=primary).delete()
    context = {"sides": Side_Menu.objects.all(),
            "drinks": Drink_Menu.objects.all(),
            "veggies": Veggie_Menu.objects.all(),
            "sauces": Sauce_Menu.objects.all(),
            "patties": Patty_Menu.objects.all(),
            "buns": Buns_Menu.objects.all(),
    }
    return render(request,'menu.html', context) 


# def createBurgerOrder(request):
        
#     form = VeggieForm()
#     if request.method == 'POST':
#         form = VeggieForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/home/menu/')

#     context = {'form':form}
#     return render(request,'addUpdateVeggie.html', context) 