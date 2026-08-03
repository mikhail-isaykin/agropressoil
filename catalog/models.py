from django.db import models
from django.urls import reverse
from slugify import slugify


class Product(models.Model):
    class Category(models.TextChoices):
        KOMPLEKSNYE = 'kompleksnye-resheniya', 'Комплексные решения'
        PRESSOVANIE = 'pressovanie', 'Прессование'
        PODGOTOVKA = 'podgotovka-syrya', 'Подготовка сырья'
        OCHISTKA = 'ochistka-masla', 'Очистка масла'
        UTILIZATSIYA = 'utilizatsiya-othodov', 'Утилизация отходов, лузги и получение тепловой энергии'
        ZAPCHASTI = 'zapchasti-i-emkosti', 'Запчасти и ёмкости'

    title = models.CharField('Заголовок', max_length=200)
    slug = models.SlugField('Адрес (slug)', max_length=200, unique=True, blank=True)
    category = models.CharField('Категория', max_length=30, choices=Category.choices)
    featured_image = models.ImageField('Hero-картинка', upload_to='work/', blank=True)
    sidebar_text = models.TextField('Текст в сайдбаре', blank=True)
    body = models.TextField('Тело (HTML: текст + картинки + галереи)')
    published = models.BooleanField('Опубликовано', default=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Запись каталога'
        verbose_name_plural = 'Каталог'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('catalog:product_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)
            slug, n = base, 1
            while Product.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                n += 1
                slug = f'{base}-{n}'
            self.slug = slug
        super().save(*args, **kwargs)
