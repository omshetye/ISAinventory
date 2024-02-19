# Generated by Django 5.0 on 2024-02-19 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_remove_contactmessage_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalVar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variable_name', models.CharField(max_length=100, unique=True)),
                ('key_value', models.CharField(max_length=255)),
            ],
        ),
    ]
