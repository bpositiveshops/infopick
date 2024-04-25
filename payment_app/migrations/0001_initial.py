# Generated by Django 5.0.4 on 2024-04-25 10:58

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('infopick_app', '0010_delete_clientqrcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, verbose_name='Customer Name')),
                ('amount', models.FloatField(verbose_name='Amount')),
                ('status', models.CharField(default='Pending', max_length=254, verbose_name='Payment Status')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('provider_order_id', models.CharField(max_length=40, verbose_name='Order ID')),
                ('payment_id', models.CharField(max_length=36, verbose_name='Payment ID')),
                ('signature_id', models.CharField(max_length=128, verbose_name='Signature ID')),
                ('clientid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='infopick_app.client')),
            ],
        ),
    ]
