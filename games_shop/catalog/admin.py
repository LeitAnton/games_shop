from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = (
        "id",
        "title",
    )
    list_editable = (
        "title",
    )
    search_fields = (
        "title",
        "description",
    )
    prepopulated_fields = {
        "slug":(
            "title",
        )
    }


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product

    list_display = (
        "id",
        "title",
        "price",
        "category",
        "date_release",
        "date_publish",
    )
    list_filter = (
        "price",
        "category",
        "date_release",
        "date_publish",
    )
    list_editable = (
        "title",
        "slug",
        "price",
        "date_publish",
        "date_release",
    )
    search_fields = (
        "title",
        "description",
        "price",
        "date_release",
    )
    prepopulated_fields = {
        "slug":(
            "title",
        )
    }
    date_hierarchy = "date_publish"
