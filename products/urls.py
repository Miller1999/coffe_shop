from .views import ProductFormView, ProductListView
from django.urls import path

# Esto se crea con el fin de separar las urls por app

urlpatterns = [
    path("", ProductListView.as_view(), name="list_product"),
    path("add/", ProductFormView.as_view(), name="add_product"),
]
