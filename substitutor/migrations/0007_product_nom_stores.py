# Generated by Django 3.1.3 on 2020-11-13 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('substitutor', '0006_product_nutriments'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='nom_stores',
            field=models.TextField(null=True),
        ),
    ]
