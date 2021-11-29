from django.forms import ModelForm
from .models import Customer, Drink_Menu, Order, Side_Menu

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class SideForm(ModelForm):
    class Meta:
        model = Side_Menu
        fields = '__all__'

class DrinkForm(ModelForm):
    class Meta:
        model = Drink_Menu
        fields = '__all__'
