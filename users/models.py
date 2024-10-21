from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, verbose_name="username", blank=True, null=True)
    email = models.EmailField(unique=True, verbose_name="Email", help_text="Введите свой Email (обязательное поле)")
    phone_number = models.CharField(max_length=35, verbose_name="Phone number", blank=True, null=True, help_text="Введите номер телефона")
    country = models.CharField(max_length=35, blank=True, null=True, help_text="Введите страну")
    avatar = models.ImageField(upload_to="users/avatars/", blank=True, null=True, help_text="Загрузите свой аватар")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
