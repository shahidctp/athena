# Generated by Django 3.2.5 on 2021-10-14 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customerapp', '0003_delete_cus_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cussignup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=16)),
                ('confirm_password', models.CharField(max_length=16)),
            ],
        ),
    ]
