from django.shortcuts import render

from .models import Customer

def index(request):
    context = {"customers": Customer.objects.all()}
    return render(request, "index.html", context)