# Generated by Django 5.0.3 on 2024-03-25 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_rename_promotion_product_promotions_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='last_updated',
            new_name='last_update',
        ),
    ]