# Generated by Django 3.0.8 on 2020-07-24 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0004_message_previuos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='previuos',
            new_name='previous',
        ),
    ]
