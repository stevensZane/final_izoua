# Generated by Django 5.1.4 on 2024-12-24 14:57

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id_client', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('adress', models.CharField(blank=True, default='', max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'client',
            },
        ),
        migrations.CreateModel(
            name='DailyInventory',
            fields=[
                ('inventaire_id', models.AutoField(primary_key=True, serialize=False)),
                ('small_pizzas_count', models.IntegerField(default=0)),
                ('large_pizzas_count', models.IntegerField(default=0)),
                ('sold_small_pizzas_count', models.IntegerField(default=0)),
                ('sold_large_pizzas_count', models.IntegerField(default=0)),
                ('date', models.DateField(default=django.utils.timezone.now, unique=True)),
            ],
            options={
                'verbose_name': 'Inventaire',
            },
        ),
        migrations.CreateModel(
            name='DeliveryPerson',
            fields=[
                ('id_deliveryman', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(default='', max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('add_at', models.DateField(default=django.utils.timezone.now, max_length=50)),
            ],
            options={
                'verbose_name': 'livreur',
            },
        ),
        migrations.CreateModel(
            name='ExtraTopping',
            fields=[
                ('extratopping_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('price', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Supplément',
            },
        ),
        migrations.CreateModel(
            name='PizzaName',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='Pizza normale', max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Noms des pizza',
            },
        ),
        migrations.CreateModel(
            name='PizzaSizePrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Petite', models.IntegerField(default=0)),
                ('Grande', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Prix par taille de pizza',
            },
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('pizza_id', models.AutoField(primary_key=True, serialize=False)),
                ('moitie_1', models.CharField(blank=True, max_length=50, null=True)),
                ('moitie_2', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(choices=[('Spéciale', 'Spéciale'), ('Normale', 'Normale')], default='Normale', max_length=50)),
                ('name', models.CharField(default='Pizza normale', max_length=50)),
                ('size', models.CharField(choices=[('Grande', 'Grande'), ('Petite', 'Petite')], default='Grande', max_length=50)),
                ('extratoppings', models.ManyToManyField(to='izouapp.extratopping')),
            ],
            options={
                'verbose_name': 'pizzas achetée',
            },
        ),
        migrations.CreateModel(
            name='orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('deliveryHour', models.TimeField(blank=True, null=True)),
                ('deliveryAdress', models.CharField(blank=True, max_length=50, null=True)),
                ('payment_method', models.CharField(blank=True, choices=[('izoua', 'Izoua'), ('delivered_man', 'Livreur')], max_length=50, null=True)),
                ('create_at', models.DateField(default=django.utils.timezone.now)),
                ('update_at', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('surplace', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('delivered', 'Livrée'), ('canceled', 'Annulée'), ('on-site', 'Sur place')], default='delivered', max_length=50)),
                ('edit_requested', models.BooleanField(default=False)),
                ('deliveryPrice', models.IntegerField(blank=True, default=0, null=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='izouapp.client')),
                ('deliveryPerson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='izouapp.deliveryperson')),
                ('pizzas', models.ManyToManyField(to='izouapp.pizza')),
            ],
            options={
                'verbose_name': 'commande',
            },
        ),
    ]
