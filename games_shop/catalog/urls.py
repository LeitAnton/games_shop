from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.catalog, name="catalog"),
    path('categories/', views.categories, name="categories"),
    path('cart/', views.catalog, name="cart"),
]
