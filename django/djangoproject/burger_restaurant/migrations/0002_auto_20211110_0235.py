# Generated by Django 3.2.8 on 2021-11-10 02:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('burger_restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('phone_num', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='status',
            name='profile',
        ),
        migrations.DeleteModel(
            name='Poke',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]
