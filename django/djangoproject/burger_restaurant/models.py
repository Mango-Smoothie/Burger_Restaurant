import uuid

from django.db import models


class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Name", max_length=100)
    phone_num = models.CharField("Phone Number", max_length=10)

    class Meta:
        verbose_name_plural = "Customers"

    # controls how to use the 
    def __str__(self):
        return "<{} - {}>".format(
            self.name, self.phone_num)

class Order(models.Model):
    STATUS = (
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Finished', 'Finished')
    )

    order_num = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_status = models.CharField("Order Status", max_length=100, choices=STATUS)
    total_price = models.DecimalField("Total Price", max_digits=10, decimal_places=2)
    customer = models.ForeignKey(Customer, null=False, on_delete=models.CASCADE)

    # controls how to use the 
    def __str__(self):
        return format(self.order_num)


class Drink_Menu(models.Model):
    drink_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    drink_name = models.CharField("Drink Name", max_length=100)
    d_price = models.DecimalField("Price", max_digits=10, decimal_places=2)
    def __str__(self):
        return self.drink_name

class Drink_Order(models.Model):
    order_number = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    drink_name = models.ForeignKey(Drink_Menu, null=False, on_delete=models.CASCADE)
    d_quantity = models.IntegerField("Quantity")

    @property
    def drink_total(self):
        return self.d_quantity * self.drink_name.d_price

class Side_Menu(models.Model):
    side_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    side_name = models.CharField("Side Name", max_length=100)
    s_price = models.DecimalField("Price", max_digits=10, decimal_places=2)

    def __str__(self):
        return self.side_name

class Side_Order(models.Model):
    order_number = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    side_name = models.ForeignKey(Side_Menu, null=False, on_delete=models.CASCADE)
    s_quantity = models.IntegerField("Quantity")

    @property
    def side_total(self):
        return self.s_quantity * self.side_name.s_price

class Veggie_Menu(models.Model):
    veggie_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    veggie_name = models.CharField("Vegetable Name", max_length=100)
    veggie_price = models.DecimalField("Price", max_digits=10, decimal_places=2)

    def __str__(self):
        return self.veggie_name

class Patty_Menu(models.Model):
    patty_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patty_name = models.CharField("Patty Name", max_length=100)
    p_price = models.DecimalField("Price", max_digits=10, decimal_places=2)
    def __str__(self):
        return self.patty_name

class Buns_Menu(models.Model):
    buns_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    buns_name = models.CharField("Buns Name", max_length=100)
    b_price = models.DecimalField("Price", max_digits=10, decimal_places=2)
    def __str__(self):
        return self.buns_name

class Sauce_Menu(models.Model):
    sauce_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sauce_name = models.CharField("Sauce Name", max_length=100)
    s_price = models.DecimalField("Price", max_digits=10, decimal_places=2)
    def __str__(self):
        return self.sauce_name

class Burger_Order(models.Model):
    order_number = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    patty = models.ForeignKey(Patty_Menu, null=False, on_delete=models.CASCADE)
    buns = models.ForeignKey(Buns_Menu, null=False, on_delete=models.CASCADE)
    veggies = models.ForeignKey(Veggie_Menu, null=False, on_delete=models.CASCADE)
    sauce = models.ForeignKey(Sauce_Menu, null=False, on_delete=models.CASCADE)
    b_quantity = models.IntegerField("Quantity")

    @property
    def burger_total(self):
        return self.b_quantity * (self.sauce.s_price + self.buns.b_price + self.patty.p_price + self.veggies.veggie_price)
