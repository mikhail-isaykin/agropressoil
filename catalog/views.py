from django.views.generic import DetailView, ListView

from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'
    paginate_by = 16

    def get_queryset(self):
        qs = Product.objects.filter(published=True)
        category = self.request.GET.get('category')
        if category:
            qs = qs.filter(category=category)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['categories'] = Product.Category.choices
        ctx['current_category'] = self.request.GET.get('category', '')
        return ctx


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

    def get_queryset(self):
        return Product.objects.filter(published=True)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        qs = Product.objects.filter(published=True)
        ctx['prev'] = qs.filter(title__lt=self.object.title).last() or qs.last()
        ctx['next'] = qs.filter(title__gt=self.object.title).first() or qs.first()
        return ctx
