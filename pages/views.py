from django.views.generic import TemplateView

from catalog.models import Product
from news.models import Item


class HomeView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['products'] = Product.objects.filter(published=True)[:16]
        ctx['news'] = Item.objects.all()[:4]
        return ctx


class MaslopressyView(TemplateView):
    template_name = 'pages/maslopressy.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['presses'] = Product.objects.filter(category=Product.Category.PRESSOVANIE, published=True)
        return ctx
