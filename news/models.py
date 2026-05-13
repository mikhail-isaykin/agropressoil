from django.db import models
from core.utils import convert_to_webp, generate_slug


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.image:
            self.image = convert_to_webp(self.image)
        if not self.slug:
            self.slug = generate_slug(self.title)
        super().save(*args, **kwargs)
