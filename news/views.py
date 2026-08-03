# news/views.py
from django.views.generic import DetailView, ListView

from .models import Item


class NewsListView(ListView):
    model = Item
    template_name = 'news/news_list.html'
    context_object_name = 'news'
    paginate_by = 20


class NewsDetailView(DetailView):
    model = Item
    template_name = 'news/news_detail.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['recent'] = Item.objects.exclude(pk=self.object.pk)[:5]
        return ctx
