from django.db import models
from core.utils import convert_to_webp, generate_slug


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Категория')
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
    order = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='Порядок отображения',
        help_text='Чем меньше число, тем левее карточка'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['order', 'id']

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.image:
            self.image = convert_to_webp(self.image)
        if not self.slug:
            self.slug = generate_slug(self.title)
        super().save(*args, **kwargs)


class Product(models.Model):
    category = models.ForeignKey(
        'Category', on_delete=models.CASCADE, related_name='products'
    )
    title = models.CharField(max_length=50, verbose_name='Продукт')
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    order = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='Порядок отображения',
        help_text='Чем меньше число, тем левее карточка'
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Подукты'
        ordering = ['order', 'id']

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.image:
            self.image = convert_to_webp(self.image)
        if not self.slug:
            self.slug = generate_slug(self.title)
        super().save(*args, **kwargs)


class Part(models.Model):
    product = models.ForeignKey(
        'Product', on_delete=models.CASCADE, related_name='parts'
    )
    title = models.CharField(max_length=50, verbose_name='Запчасть')
    image = models.ImageField(upload_to='parts/', blank=True, null=True)
    order = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='Порядок отображения',
        help_text='Чем меньше число, тем левее карточка'
    )

    class Meta:
        verbose_name = 'Запчасть'
        verbose_name_plural = 'Запчасти'
        ordering = ['order', 'id']

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.image:
            self.image = convert_to_webp(self.image)
        super().save(*args, **kwargs)
