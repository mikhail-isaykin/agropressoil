from django.views.generic import ListView
from .models import News


class NewsView(ListView):
    model = News
    template_name = 'news/news.html'
    context_object_name = 'news'
