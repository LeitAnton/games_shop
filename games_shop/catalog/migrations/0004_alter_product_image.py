# Generated by Django 4.1.2 on 2022-10-22 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
