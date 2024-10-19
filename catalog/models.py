from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=100, verbose_name="Наименование категории", help_text="Введите наименование категории")
    description = models.CharField(max_length=150, verbose_name="Описание категории", help_text="Опишите категорию")

    def __str__(self):
        return f"{self.name} {self.description}"

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["name"]


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование продукта")
    description = models.CharField(max_length=150, verbose_name="Описание продукта")
    image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name="Изображение")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, verbose_name="Категория продукта", related_name="products")
    price = models.IntegerField(verbose_name="Цена продукта")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.description} {self.category}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name"]
