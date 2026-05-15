from django.test import TestCase, Client
from django.urls import reverse
from catalog.models import Category, Product


class CatalogViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(title='Техника')
        self.product = Product.objects.create(title='Продукт А', category=self.category, order=1)

    def test_catalog_view_returns_200(self):
        response = self.client.get(reverse('catalog'))
        self.assertEqual(response.status_code, 200)

    def test_category_view_returns_200(self):
        response = self.client.get(reverse('category', kwargs={'category_slug': self.category.slug}))
        self.assertEqual(response.status_code, 200)

    def test_category_view_contains_products(self):
        response = self.client.get(reverse('category', kwargs={'category_slug': self.category.slug}))
        self.assertIn(self.product, response.context['products'])

    def test_product_view_returns_200(self):
        response = self.client.get(reverse('product', kwargs={
            'category_slug': self.category.slug,
            'product_slug': self.product.slug
        }))
        self.assertEqual(response.status_code, 200)
