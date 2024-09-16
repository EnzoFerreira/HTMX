from django.urls import path

from products import views

urlpatterns = [
    path('products_list', views.products_list)
]