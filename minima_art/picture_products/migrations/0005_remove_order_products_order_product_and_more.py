# Generated by Django 5.1.2 on 2024-12-09 20:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picture_products', '0004_order_size_order_wishes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='picture_products.product'),
        ),
        migrations.AddField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
