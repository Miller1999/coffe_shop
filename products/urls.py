from .views import ProductFormView
from django.urls import path

# Esto se crea con el fin de separar las urls por app

urlpatterns = [
    path("add/", ProductFormView.as_view(), name="add_product"),
]
