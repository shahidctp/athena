# Generated by Django 3.2.5 on 2021-10-15 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Customerapp', '0007_remove_cussignin_full_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cussignup',
            old_name='full_name',
            new_name='username',
        ),
    ]
