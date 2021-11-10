import uuid

from django.db import models


class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=10)


    def __str__(self):
        return "<Customer id={} Name={} Phone Number={}>".format(
            self.id, self.name, self.phone_num
        )

class Order(models.Model):
    order_num = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_status = models.CharField(max_length=100)
    total_price = models.IntegerField() # need to change to allow floats.!!!!!!!!
    customer = models.ForeignKey(Customer, null=False, on_delete=models.CASCADE)

class Drink_Menu(models.Model):
    drink_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    drink_name = models.CharField(max_length=100)
    d_price = models.IntegerField()

class Drink_Order(models.Model):
    order_number = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    drink_name = models.ForeignKey(Drink_Menu, null=False, on_delete=models.CASCADE)
    d_quantity = models.IntegerField()

class Side_Menu(models.Model):
    side_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    side_name = models.CharField(max_length=100)
    s_price = models.IntegerField()

class Side_Order(models.Model):
    order_number = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    side_name = models.ForeignKey(Side_Menu, null=False, on_delete=models.CASCADE)
    s_quantity = models.IntegerField()

class Veggie_Menu(models.Model):
    veggie_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    veggie_name = models.CharField(max_length=100)
    veggie_price = models.IntegerField()

class Patty_Menu(models.Model):
    patty_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patty_name = models.CharField(max_length=100)
    p_price = models.IntegerField()

class Buns_Menu(models.Model):
    buns_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    buns_name = models.CharField(max_length=100)
    b_price = models.IntegerField()

class Sauce_Menu(models.Model):
    sauce_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sauce_name = models.CharField(max_length=100)
    s_price = models.IntegerField()

class Burger_Order(models.Model):
    order_number = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    patty = models.ForeignKey(Patty_Menu, null=False, on_delete=models.CASCADE)
    buns = models.ForeignKey(Buns_Menu, null=False, on_delete=models.CASCADE)
    veggies = models.ForeignKey(Veggie_Menu, null=False, on_delete=models.CASCADE)
    sauce = models.ForeignKey(Sauce_Menu, null=False, on_delete=models.CASCADE)
    b_quantity = models.IntegerField()



#     @property
#     def latest_status(self):
#         return self.status_set.order_by("-date_time").first()


# class Status(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     message = models.TextField()
#     date_time = models.DateTimeField()
#     profile = models.ForeignKey(Profile, null=False, on_delete=models.CASCADE)

#     class Meta:
#         verbose_name_plural = "Statuses"

#     def __str__(self):
#         return f"<Status from={self.profile_id} at={self.date_time}>"


# class Poke(models.Model):
#     poker = models.ForeignKey(
#         Profile, null=False, on_delete=models.CASCADE, related_name="poke_poker"
#     )
#     pokee = models.ForeignKey(
#         Profile, null=False, on_delete=models.CASCADE, related_name="poke_pokee"
#     )
#     date_time = models.DateTimeField()

#     def __str__(self):
#         return f"<Poke from={self.poker_id} to={self.pokee_id} at={self.date_time}>"
