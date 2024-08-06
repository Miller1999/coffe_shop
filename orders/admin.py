from django.contrib import admin
from .models import Order, OrderProduct

# Register your models here.
# Se registran los modelos para poder usarlos en el admin page


# Este tabular line es para poder usar un modelo dentro de otro
class OrderProductInlineAdmin(admin.TabularInline):
    model = OrderProduct
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    model = Order
    # Aqui se registran los modelos hijos
    inlines = [OrderProductInlineAdmin]


admin.site.register(Order, OrderAdmin)
