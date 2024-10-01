# Generated by Django 5.1.1 on 2024-10-01 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_alter_category_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(
                blank=True,
                help_text="Вставьте изображение продукта",
                null=True,
                upload_to="images/",
                verbose_name="Изображение",
            ),
        ),
    ]
