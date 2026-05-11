from django.views.generic import ListView, DetailView
from .models import Category, Product


class CatalogView(ListView):
    model = Category
    template_name = 'catalog/catalog.html'
    context_object_name = 'catalog'

class CategoryView(DetailView):
    model = Category
    template_name = 'catalog/category.html'
    context_object_name = 'category'
    slug_url_kwarg = 'category_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = self.object.products.all()
        return context

class ProductView(DetailView):
    model = Product
    template_name = 'catalog/product.html'
    context_object_name = 'product'
    slug_url_kwarg = 'product_slug'
