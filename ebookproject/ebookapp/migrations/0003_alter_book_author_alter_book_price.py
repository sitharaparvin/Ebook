# Generated by Django 4.2.6 on 2023-10-29 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebookapp', '0002_alter_book_author_alter_book_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.CharField(max_length=100),
        ),
    ]