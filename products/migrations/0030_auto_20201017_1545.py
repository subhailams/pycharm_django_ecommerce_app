# Generated by Django 2.2.8 on 2020-10-17 10:15

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0029_auto_20201017_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=products.models.upload_image_path),
        ),
    ]
