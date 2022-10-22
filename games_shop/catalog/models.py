from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name="Category", null=True)
    date_release = models.DateField()
    date_publish = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True)
