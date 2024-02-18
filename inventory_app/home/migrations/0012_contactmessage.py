# Generated by Django 4.0 on 2024-02-18 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_member_otp_created_at_member_otp_secret'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.IntegerField()),
                ('message', models.TextField()),
            ],
        ),
    ]