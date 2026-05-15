from django.test import TestCase
from catalog.models import Category


class CategoryModelTest(TestCase):
    def test_slug_auto_generated(self):
        category = Category.objects.create(title='Тестовая категория')
        self.assertTrue(category.slug)
