# Generated by Django 5.1.2 on 2024-12-03 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picture_products', '0002_galleryimage_created_at_galleryimage_updated_at_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomerProfile',
        ),
    ]
