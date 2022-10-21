from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name="Category")
    date_release = models.DateTimeField()
    date_publish = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True)
