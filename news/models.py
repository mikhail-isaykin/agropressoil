from django.db import models
from django.urls import reverse
from django.utils import timezone
from slugify import slugify


class Item(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    slug = models.SlugField('Адрес (slug)', max_length=200, unique=True)
    image = models.ImageField('Картинка', upload_to='news/', blank=True)
    teaser = models.TextField('Анонс', blank=True)
    body = models.TextField('Текст статьи')
    published = models.DateField('Дата публикации', default=timezone.now)

    class Meta:
        ordering = ['-published']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news:news_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)
            slug = base
            n = 1
            while Item.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                n += 1
                slug = f'{base}-{n}'
            self.slug = slug
        super().save(*args, **kwargs)
