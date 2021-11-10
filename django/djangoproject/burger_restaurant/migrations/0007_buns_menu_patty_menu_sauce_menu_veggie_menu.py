# Generated by Django 3.2.8 on 2021-11-10 02:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('burger_restaurant', '0006_side_menu_side_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buns_Menu',
            fields=[
                ('buns_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('buns_name', models.CharField(max_length=100)),
                ('b_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Patty_Menu',
            fields=[
                ('patty_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('patty_name', models.CharField(max_length=100)),
                ('p_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sauce_Menu',
            fields=[
                ('sauce_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('sauce_name', models.CharField(max_length=100)),
                ('s_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Veggie_Menu',
            fields=[
                ('veggie_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('veggie_name', models.CharField(max_length=100)),
                ('veggie_price', models.IntegerField()),
            ],
        ),
    ]
