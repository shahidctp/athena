# Generated by Django 3.2.5 on 2021-12-21 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_app', '0005_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='commented_in',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Blog_app.post'),
        ),
    ]
