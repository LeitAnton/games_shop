from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from .models import Product, Category
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page


@cache_page(20, key_prefix="page")
def catalog(request):
    products_list = Product.objects.all()
    paginator = Paginator(products_list, 6)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    return render(request, "catalog.html", {"paginator":paginator, "page":page})


@cache_page(20, key_prefix="page")
def categories(request):
    categories = Category.objects.all()
    products_list = Product.objects.all()
    paginator = Paginator(products_list, 6)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    return render(request, "categories.html", {"paginator":paginator, "page":page, "categories":categories})


@cache_page(20, key_prefix="page")
def category(request, category_slug):
    categories = Category.objects.all()
    category = get_object_or_404(Category, slug=category_slug)
    products_list = Product.objects.filter(category=category)
    paginator = Paginator(products_list, 6)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    return render(request, "categories.html", {"paginator":paginator, "page":page, "category": category, "categories":categories})


def cart(request):
    return redirect("catalog.html")


def product(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, "product.html", {"product":product})