from django.db.models import fields
from django.forms import ModelForm
from .models import Burger_Order, Customer, Drink_Menu, Drink_Order, Order, Side_Menu, Side_Order, Veggie_Menu, Buns_Menu, Sauce_Menu, Patty_Menu

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

class VeggieForm(ModelForm):
    class Meta:
        model = Veggie_Menu
        fields = '__all__'

class BunsForm(ModelForm):
    class Meta:
        model = Buns_Menu
        fields = '__all__'

class SauceForm(ModelForm):
    class Meta:
        model = Sauce_Menu
        fields = '__all__'

class PattyForm(ModelForm):
    class Meta:
        model = Patty_Menu
        fields = '__all__'


class SideOrderForm(ModelForm):
    class Meta:
        model = Side_Order
        fields = '__all__'

        # fields = ['side_name', 's_quantity']

class DrinkOrderForm(ModelForm):
    class Meta:
        model = Drink_Order
        fields = '__all__'
        # fields = ['drink_name', 'd_quantity']

class BurgerOrderForm(ModelForm):
    class Meta:
        model = Burger_Order
        fields = '__all__'
        # fields = ['patty', 'buns', 'veggies', 'sauce', 'b_quantity']