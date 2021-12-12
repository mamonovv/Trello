# Generated by Django 3.2.9 on 2021-12-10 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20211211_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boards',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название доски'),
        ),
        migrations.AlterField(
            model_name='card',
            name='board',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.boards', verbose_name='Название доски'),
        ),
        migrations.AlterField(
            model_name='card',
            name='column',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.column', verbose_name='Название колонки'),
        ),
        migrations.AlterField(
            model_name='card',
            name='content',
            field=models.TextField(verbose_name='Контент'),
        ),
        migrations.AlterField(
            model_name='card',
            name='deadline',
            field=models.DateTimeField(verbose_name='Срок выполнения'),
        ),
        migrations.AlterField(
            model_name='card',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название карточки'),
        ),
        migrations.AlterField(
            model_name='card',
            name='photo',
            field=models.ImageField(upload_to='photos/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='column',
            name='board',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.boards', verbose_name='Название доски'),
        ),
        migrations.AlterField(
            model_name='column',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название Колонки'),
        ),
    ]