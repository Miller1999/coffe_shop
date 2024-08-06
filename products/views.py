from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from .forms import ProductForm
from products.models import Product

# Create your views here.
# Se usa form_valid para validar el form
# Se usa success_url para redireccionar a otra pagina en caso de que el form sea satisfactorio


class ProductFormView(generic.FormView):
    template_name = "products/add_products.html"
    form_class = ProductForm
    success_url = reverse_lazy("add_product")

    def form_valid(self, form: any) -> HttpResponse:
        form.save()
        return super().form_valid(form)


class ProductListView(generic.ListView):
    model = Product
    template_name = "products/list_product.html"
    context_object_name = "products"
