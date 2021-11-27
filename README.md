# Burger_Restaurant
WebApp for CSCI220: Database Management and Systems Design 

If this is your first time using this webapp.
Step1:
## Step 1: Secure Configuration

It is a terrible idea to run software with default passwords. To configure the password for the database and other settings, you will need to write them in a `.env` file. Follow these steps:

1. Copy `dot_env_example` to `.env`
2. Run `chmod 600 .env` to prevent other users from reading your `.env` file
3. Edit `.env`, changing:
  - The text `RANDOM_PASSWORD` to a password which is actually random
  - The text `SOMETHING_LONG_AND_RANDOM` to random text, ideally generated using the Python one-liner below:

```
python3 -c "import string,random; uni=string.ascii_letters+string.digits; print(''.join([random.SystemRandom().choice(uni) for i in range(random.randint(45,50))]))"
```

## Step 2: Start the Docker Services

Run:
```
docker compose up
```

The first time you run it, this command will take a few minutes to complete. This is because Docker needs to download the code for PostgresSQL, etc.

When you are done running the application, you can stop it by typing `Control-C`.

When loading the following pages, you will get errors but continue to step 3 to fix them.
Load <http://localhost:8080> and you should be redirected to the "Django administration" login interface.

Load <http://localhost:8080/home> to view the latest statuses of users of the minifacebook application. See instructions below for using the Django admin interface, which you can use to create users and status updates. 

## Step 3: Migrate then create superuser

Note: Do all of step 3 while the docker container is running.

Run this line in the root directory of the project
```
docker compose exec django python manage.py migrate
```

Create your superuser which will be able to acess the Django admin interface:

```
docker compose exec django python manage.py createsuperuser
```

```
docker compose exec django python manage.py makemigrations
```



{% if orders %}
<table>
<tr><th>Order Number</th><th>Order Status</th><th>Total Price</th><th>Customer Phone Number</th><th>Update</th><th>Delete</th></tr>
{% for order in orders %}
  <tr>
    <td>{{order.order_num}}</td>
    <td>{{order.order_status}}</td>
    <td>{{order.total_price}}</td>
    <td>{{order.customer}}</td>
    <!-- <td> <button type="button">Add Student</button> </td> -->
    <!-- <td> <a href="{% url 'update_customer' customer.id%}"><button>Update Customer</button></a></td> -->
    <td> <button type="button">Edit Order</button> </td>
    <td> <button type="button">Delete Order</button> </td>


  </tr>
{% endfor %}
</table>
<!-- <a href="{% url 'add_customer' %}">
<button>Add Customer</button></a> -->
<button type="button">Add Order</button></a>

{% else %}
  <p>No Order.</p>
  <!-- <a href="{% url 'add_customer' %}">
    <button>Add Customer</button></a> -->
  <button type="button">Add Order</button></a>

{% endif %}

