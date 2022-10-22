from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.catalog, name="catalog"),
    path('product/<int:product_id>/', views.product, name="product"),
    path('categories/', views.categories, name="categories"),
    path('cart/', views.catalog, name="cart"),
]
