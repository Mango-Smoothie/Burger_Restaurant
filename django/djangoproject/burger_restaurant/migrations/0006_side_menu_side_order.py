# Generated by Django 3.2.8 on 2021-11-10 02:53

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('burger_restaurant', '0005_drink_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Side_Menu',
            fields=[
                ('side_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('side_name', models.CharField(max_length=100)),
                ('s_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Side_Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_quantity', models.IntegerField()),
                ('order_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='burger_restaurant.order')),
                ('side_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='burger_restaurant.side_menu')),
            ],
        ),
    ]
