from django.db import models


class Category(models.Model):

    name = models.CharField(
        max_length=100,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории",
    )
    description = models.CharField(
        max_length=150, verbose_name="Описание категории", help_text="Опишите категорию"
    )

    def __str__(self):
        return f"{self.name} {self.description}"

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ("name",)


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование продукта",
        help_text="Введите наименование продукта",
    )
    description = models.CharField(
        max_length=150, verbose_name="Описание продукта", help_text="Опишите продукт"
    )
    image = models.ImageField(
        upload_to='products/',
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Вставьте изображение продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Категория продукта",
        help_text="Введите категорию продукта",
        related_name="products",
    )
    price = models.IntegerField(
        verbose_name="Цена продукта", help_text="Введите цену продукта"
    )
    created_at = models.DateField(
        verbose_name="Дата создания продукта в БД",
        help_text="Введите дату создания продукта",
    )
    updated_at = models.DateField(
        verbose_name="Дата изменения продукта в БД",
        help_text="Введите дату изменения продукта",
    )

    def __str__(self):
        return f"{self.name} {self.description} {self.category}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name"]
