# Generated by Django 3.0.8 on 2020-07-30 16:28

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0010_auto_20200730_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authority',
            name='photo',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='message',
            name='attachment',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='auto'),
        ),
    ]
