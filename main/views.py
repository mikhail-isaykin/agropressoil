from django.views.generic import TemplateView
from catalog.models import Category
from news.models import News
from contacts.forms import ContactForm


class HomeView(TemplateView):
    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['catalog'] = Category.objects.all()[:3]
        context['news'] = News.objects.all()[:4]
        context['form'] = ContactForm()
        return context
