# Generated by Django 5.0.3 on 2024-03-25 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip_code',
            field=models.PositiveSmallIntegerField(default=None, null=True),
        ),
    ]
