from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="E-mail")

    avatar = models.ImageField(upload_to="users/avatar", verbose_name="Аватар", null=True, blank=True, help_text='Загрузите свой аватар')
    phone_number = PhoneNumberField(unique=True, verbose_name="Номер телефона", null=True, blank=True, help_text='Введите номер телефона')
    country = models.CharField(max_length=100, verbose_name="Страна", null=True, blank=True, help_text='Введите страну')

    token = models.CharField(max_length=100, verbose_name="Токен", null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email

