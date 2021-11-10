from django.contrib import admin

from .models import Buns_Menu, Burger_Order, Customer, Drink_Order, Order , Drink_Menu, Patty_Menu, Sauce_Menu, Side_Menu, Side_Order, Veggie_Menu#, Profile, Status, Poke

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Drink_Menu)
admin.site.register(Drink_Order)
admin.site.register(Side_Menu)
admin.site.register(Side_Order)
admin.site.register(Patty_Menu)
admin.site.register(Sauce_Menu)
admin.site.register(Buns_Menu)
admin.site.register(Veggie_Menu)
admin.site.register(Burger_Order)