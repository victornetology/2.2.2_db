from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title

class Tag(models.Model):
   name = models.CharField(max_length=80, verbose_name='tag')

   class Meta:
       verbose_name = 'Теги'
       verbose_name_plural = 'Теги'

   def __str__(self):
       return self.name


class Scope(models.Model):
   is_main =  models.BooleanField(default=0, verbose_name='Основной')
   tag = models.ForeignKey(Tag,  on_delete=models.CASCADE)
   article = models.ForeignKey(Article, on_delete=models.CASCADE)
   #article = models.ManyToManyField(Article)

   class Meta:
       verbose_name = 'Теги к статье'
       verbose_name_plural = 'Теги к статье'
       ordering = ['-is_main', 'tag']

   def __str__(self):
       return self.tag.name