# Generated by Django 3.0.8 on 2020-07-24 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0006_auto_20200724_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='threads', to='threads.Topic'),
        ),
    ]
