from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('catalog/', include('catalog.urls')),
    path('repair/', TemplateView.as_view(template_name='repair/repair.html'), name='repair'),
    path('news/', include('news.urls')),
    path('about/', TemplateView.as_view(template_name='about/about.html'), name='about'),
    path('contacts/', include('contacts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
