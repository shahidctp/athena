from django.db import models


class Menu(models.Model):
    item_name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.FileField(upload_to='image')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.item_name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
