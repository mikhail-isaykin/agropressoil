from django.urls import path
from .views import CatalogView, CategoryView, ProductView


urlpatterns = [
    path('', CatalogView.as_view(), name='catalog'),
    path('<slug:category_slug>/', CategoryView.as_view(), name='category'),
    path('<slug:category_slug>/<slug:product_slug>/', ProductView.as_view(), name='product'),
]
