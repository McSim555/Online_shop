from django.db import models

from users.models import User


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
    )
    description = models.CharField(
        max_length=500,
        verbose_name="Описание продукта",
    )
    image = models.ImageField(
        upload_to="images/",
        blank=True,
        null=True,
        verbose_name="Изображение продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория продукта",
        blank=True,
        null=True,
        related_name="products",
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    owner = models.ForeignKey(User, verbose_name="Владелец", help_text="Укажите владельца продукта", blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category", "name"]
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
    )
    country = models.CharField(max_length=200, verbose_name="Страна")
    email = models.EmailField(blank=True, null=True, verbose_name="E-mail")
    phone = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Телефон"
    )
    city = models.CharField(max_length=50, verbose_name="Город")
    street = models.CharField(max_length=100, verbose_name="Улица")
    house_number = models.IntegerField(
        verbose_name="Номер дома",
    )
    postal_code = models.IntegerField(
        verbose_name="Почтовый индекс",
    )
    tax_number = models.CharField(max_length=50, verbose_name="ИНН")

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        ordering = [
            "city",
        ]

    def __str__(self):
        return f"{self.country} {self.city} {self.street} {self.house_number}"
