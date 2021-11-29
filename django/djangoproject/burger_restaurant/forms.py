from django.forms import ModelForm
from .models import Customer, Drink_Menu, Order, Side_Menu, Veggie_Menu, Buns_Menu, Sauce_Menu, Patty_Menu

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