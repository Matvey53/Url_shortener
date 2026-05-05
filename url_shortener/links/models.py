from django.db import models

class Url(models.Model):
    original_url = models.URLField(verbose_name='Оригинальный url')
    short_code = models.CharField(verbose_name='Сгенерированный короткий код')
    created_at = models.DateTimeField(verbose_name='Дата создания' ,auto_now_add=True)
    clicks = models.PositiveIntegerField(default=0, verbose_name='Счетчик переходов')
    is_active = models.BooleanField(default=True, verbose_name='Активна')
    

    class Meta:
        verbose_name = ('Ссылка')
        verbose_name_plural = ('Ссылки')

    def __str__(self):
        return self.original_url


