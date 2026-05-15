from django.test import TestCase
from catalog.models import Category, Product


class CategoryModelTest(TestCase):
    def test_slug_auto_generated(self):
        category = Category.objects.create(title='Тестовая категория')
        self.assertTrue(category.slug)

def test_products_ordered_by_order_field(self):
    category = Category.objects.create(title='Техника')
    Product.objects.create(title='Продукт А', category=category, order=3)
    Product.objects.create(title='Продукт Б', category=category, order=1)
    Product.objects.create(title='Продукт В', category=category, order=2)

    products = list(category.products.all())
    self.assertEqual(products[0].title, 'Продукт Б')
    self.assertEqual(products[1].title, 'Продукт В')
    self.assertEqual(products[2].title, 'Продукт А')
