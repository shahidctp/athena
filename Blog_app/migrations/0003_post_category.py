# Generated by Django 3.2.5 on 2021-12-17 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_app', '0002_alter_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
