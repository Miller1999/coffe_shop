from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.views.generic import DetailView

from .models import Order

# Create your views here.


class MyOrderView(DetailView):
    model = Order
    template_name = "orders/my_order.html"

    def get_object(self, queryset=None) -> Model:
        return Order.objects.filter(is_active=True).first()
