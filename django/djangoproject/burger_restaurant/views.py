from django.shortcuts import render
from django.http import HttpResponse


from .models import Customer

def index(request):
    context = {"customers": Customer.objects.all()}
    # return HttpResponse("Hello, world. You're at the Burger Restaurant index.")
    return render(request, "index.html", context)