from django.views import generic

from .models import Product


class ProductsListView(generic.ListView):
    model = Product
    context_object_name = 'products_list'
    template_name = 'products/products_list_view.html'

    def get_queryset(self):
        return Product.objects.all()


class ProductDetailView(generic.DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'products/product_detail_view.html'
