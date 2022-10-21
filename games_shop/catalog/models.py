from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name="Category")
    data_release = models.DateTimeField()
    pub_date = models.DateTimeField(auto_now=True)
