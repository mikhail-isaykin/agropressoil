from django.urls import path
from django.views.generic import TemplateView

from .views import HomeView, MaslopressyView

app_name = 'pages'

urlpatterns = [
    path('',                                      HomeView.as_view(template_name='pages/home.html'),                                              name='home'),
    path('about/',                                TemplateView.as_view(template_name='pages/about.html'),                                         name='about'),
    path('services/',                             TemplateView.as_view(template_name='pages/services.html'),                                      name='services'),
    path('contacts/',                             TemplateView.as_view(template_name='pages/contacts.html'),                                      name='contacts'),
    path('innovations/',                          TemplateView.as_view(template_name='pages/innovations/overview.html'),                          name='innovations'),
    path('innovations/dezodoratsii/',             TemplateView.as_view(template_name='pages/innovations/uchastok-dezodoratsii.html'),             name='uchastok_dezodoratsii'),
    path('innovations/rafinatsii/',               TemplateView.as_view(template_name='pages/innovations/uchastok-rafinatsii.html'),               name='uchastok_rafinatsii'),
    path('innovations/filtratsii/',               TemplateView.as_view(template_name='pages/innovations/uchastok-filtratsii.html'),               name='uchastok_filtratsii'),
    path('innovations/pressovaniya/',             TemplateView.as_view(template_name='pages/innovations/uchastok-pressovaniya.html'),             name='uchastok_pressovaniya'),
    path('innovations/podgotovki-semyan/',        TemplateView.as_view(template_name='pages/innovations/uchastok-podgotovki-semyan.html'),        name='uchastok_podgotovki_semyan'),
    path('innovations/ochistki-i-sushki-semyan/', TemplateView.as_view(template_name='pages/innovations/uchastok-ochistki-i-sushki-semyan.html'), name='uchastok_ochistki_i_sushki_semyan'),
    path('projects-video/',                       TemplateView.as_view(template_name='pages/projects/video.html'),                                name='projects_video'),
    path('projects-photo/',                       TemplateView.as_view(template_name='pages/projects/photo.html'),                                name='projects_photo'),
    path('maslopressy-dlia-otzhima-masla/',       MaslopressyView.as_view(),                                                                      name='maslopressy'),
    path('zapasnye-chasti/',                      TemplateView.as_view(template_name='pages/zapasnye-chasti.html'),                               name='zapasnye_chasti'),
]
