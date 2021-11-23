from django.shortcuts import render, redirect
from django.http import HttpResponse


from .models import Customer
from .forms import CustomerForm

def index(request):
    context = {"customers": Customer.objects.all()}
    # return HttpResponse("Hello, world. You're at the Burger Restaurant index.")
    return render(request, "index.html", context)

def createCustomer(request):
        
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/')

    context = {'form':form}
    return render(request,'addCustomer.html', context) 

def updateCustomer(request, primary):
    
    customer = Customer.objects.get(id=primary)
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance = customer)
        if form.is_valid():
            form.save()
            return redirect('/home/')

    context ={'form': form}
    return render(request,'addCustomer.html', context) 