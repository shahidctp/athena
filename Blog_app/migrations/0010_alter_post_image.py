# Generated by Django 3.2.5 on 2021-12-28 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_app', '0009_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='images', upload_to='images'),
        ),
    ]
