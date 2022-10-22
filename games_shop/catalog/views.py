from django.shortcuts import render, redirect
from django.db import models
from .models import Product, Category
from django.core.paginator import Paginator


def catalog(request):
    products_list = Product.objects.all()
    paginator = Paginator(products_list, 3)
    return render(request, "catalog.html", {"products" : })


def categories(request):
    return render(request, "categories.html")


def cart(request):
    return redirect('catalog.html')