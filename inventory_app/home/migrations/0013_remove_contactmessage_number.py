# Generated by Django 4.0 on 2024-02-18 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_contactmessage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactmessage',
            name='number',
        ),
    ]