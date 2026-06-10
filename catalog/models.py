from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание категории",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name="Наименование продукта",
        help_text="Введите наименование продукта",
    )
    description = models.CharField(
        max_length=500,
        verbose_name="Описание продукта",
        help_text="Введите описание продукта",
    )
    image = models.ImageField(
        upload_to="images/",
        blank=True,
        null=True,
        verbose_name="Изображение продукта",
        help_text="Загрузите изображение продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория продукта",
        help_text="Укажите категорию продукта",
        blank=True,
        null=True,
        related_name="products",
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category", "name"]

    def __str__(self):
        return self.name
