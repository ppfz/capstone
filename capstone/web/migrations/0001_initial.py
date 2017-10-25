# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 06:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beacon',
            fields=[
                ('Beacon_id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for Beacon', primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('Menu_id', models.CharField(help_text='Unique ID for Menu', max_length=200, primary_key=True, serialize=False)),
                ('Type', models.CharField(choices=[('BK', 'Breakfast'), ('BR', 'Brunch'), ('LN', 'Lunch'), ('DN', 'Dinner'), ('AL', 'All Day'), ('HR', 'Happy Hour')], default='AL', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Menu_Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Menu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('Order_id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for Order', primary_key=True, serialize=False)),
                ('Timestamp', models.DateTimeField(auto_now_add=True)),
                ('Table_id', models.CharField(max_length=10)),
                ('Status', models.CharField(choices=[('CK', 'Cooking'), ('DV', 'Delivered')], default='CK', max_length=2)),
            ],
            options={
                'ordering': ['Timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Order_Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField()),
                ('Order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Timestamp', models.DateTimeField(auto_now_add=True)),
                ('Pre_tips', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Tips', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('Product_id', models.CharField(help_text='Unique ID for Product', max_length=200, primary_key=True, serialize=False)),
                ('Product_name', models.CharField(max_length=200)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Description', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('Res_id', models.CharField(help_text='Unique ID for restaurant', max_length=200, primary_key=True, serialize=False)),
                ('Res_name', models.CharField(help_text='Restaurant Name', max_length=200)),
                ('Style', models.CharField(max_length=200)),
                ('Phone', models.CharField(max_length=200)),
                ('Price_range', models.CharField(max_length=10)),
                ('Business_hours', models.CharField(max_length=200)),
                ('Address', models.CharField(max_length=200)),
                ('Default_tips', models.DecimalField(decimal_places=2, default=0.15, max_digits=3)),
                ('Created_time', models.DateTimeField(auto_now_add=True)),
                ('Updated_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='order_item',
            name='Product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='Res_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Restaurant'),
        ),
        migrations.AddField(
            model_name='menu_item',
            name='Product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Product'),
        ),
        migrations.AddField(
            model_name='menu',
            name='Res_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Restaurant'),
        ),
        migrations.AddField(
            model_name='beacon',
            name='Res_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Restaurant'),
        ),
    ]