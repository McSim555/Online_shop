from django.db import models


class Article(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name="Заголовок",
        help_text="Введите заголовок статьи блога",
    )
    content = models.TextField(
        verbose_name="Содержимое",
        help_text="Введите содержимое статьи",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="images/",
        blank=True,
        null=True,
        verbose_name="Изображение (превью)",
        help_text="Загрузите изображение (превью)",
    )
    created_at = models.DateField(auto_now_add=True)
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
    views_counter = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["name"]

    def __str__(self):
        return self.name
