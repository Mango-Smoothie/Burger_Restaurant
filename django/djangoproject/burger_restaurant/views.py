from django.shortcuts import render, redirect
from django.http import HttpResponse


from .models import *
from .forms import *


def main(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if Customer.objects.filter(name=request.POST['name'], phone_num=request.POST['phone_num']).exists():
            customer = Customer.objects.get(
                name=request.POST['name'], phone_num=request.POST['phone_num'])
            return redirect('/main/customer_home/' + str(customer.id) + '/')

    context = {'form': form}
    return render(request, "customerLogin.html", context)


def home(request, primary):

    if request.method == 'POST':
        currentorder = Order.objects.create(
            order_status='Not Started', total_price=0, customer=Customer.objects.get(id=primary))
        currentorder.save()
        return redirect('/main/place_order/' + str(currentorder.order_num) + '/')

    context = {
        "customer": Customer.objects.get(id=primary),
    }
    return render(request, "customerHome.html", context)


def createCustomer(request):

    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/main/')

    context = {'form': form}
    return render(request, 'addUpdateCustomer.html', context)


def placeOrder(request, primary):
    currentOrder = Order.objects.get(order_num=primary)

    sideForm = SideOrderForm(initial={'order_number': currentOrder.order_num})
    drinkForm = DrinkOrderForm(
        initial={'order_number': currentOrder.order_num})
    burgerForm = BurgerOrderForm(
        initial={'order_number': currentOrder.order_num})

    if request.method == 'POST':
        sideForm = SideOrderForm(request.POST)
        drinkForm = DrinkOrderForm(request.POST)
        burgerForm = BurgerOrderForm(request.POST)

        if sideForm.is_valid() and drinkForm.is_valid() and burgerForm.is_valid():
            sideForm.save()
            drinkForm.save()
            burgerForm.save()
            return redirect('/main/show_order/' + str(primary) + '/')

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
    currentOrder = Order.objects.get(order_num=primary)
    burgerOrder = Burger_Order.objects.get(order_number=primary)
    sideOrder = Side_Order.objects.get(order_number=primary)
    drinkOrder = Drink_Order.objects.get(order_number=primary)

    currentOrder.total_price = burgerOrder.burger_total + \
        sideOrder.side_total + drinkOrder.drink_total
    currentOrder.save()

    context = {
        "order": currentOrder,
        "burgerOrder": burgerOrder,
        "sideOrder": sideOrder,
        "drinkOrder": drinkOrder,
    }
    return render(request, "showOrder.html", context)


def orderHistory(request, primary):
    customer = Customer.objects.get(id=primary)
    orders = Order.objects.filter(customer=customer)
    context = {
        "orders": orders,
        "customer": customer,
    }
    return render(request, "orderHistory.html", context)
