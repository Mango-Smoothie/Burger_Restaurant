# Generated by Django 3.2.8 on 2021-11-09 18:00

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('activities', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('date_time', models.DateTimeField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='burger_restaurant.profile')),
            ],
            options={
                'verbose_name_plural': 'Statuses',
            },
        ),
        migrations.CreateModel(
            name='Poke',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('pokee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poke_pokee', to='burger_restaurant.profile')),
                ('poker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poke_poker', to='burger_restaurant.profile')),
            ],
        ),
    ]