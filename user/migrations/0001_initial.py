# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-08 16:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BillingInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit_card', models.CharField(max_length=20)),
                ('card_experation_month', models.CharField(max_length=20)),
                ('card_experation_year', models.CharField(max_length=20)),
                ('billing_address', models.CharField(max_length=50)),
                ('billing_city', models.CharField(max_length=20)),
                ('billing_state', models.CharField(max_length=20)),
                ('billing_postal_code', models.CharField(max_length=20)),
                ('billing_country', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Identification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('postal_code', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lending_rating', models.DecimalField(decimal_places=2, max_digits=5)),
                ('borrowing_rating', models.DecimalField(decimal_places=2, max_digits=5)),
                ('DateStarted', models.DateTimeField()),
                ('LastLogin', models.DateTimeField()),
            ],
        ),
    ]
